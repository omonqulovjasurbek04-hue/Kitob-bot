import random

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from data.questions import QUESTIONS
from keyboards.keyboards import quiz_keyboard, quiz_next_keyboard
from utils.storage import add_correct_answer, add_wrong_answer, get_stats_text

router = Router()


@router.message(F.text == "❓ Test")
async def start_test(message: Message):
    """Test savolini yuboradi."""
    await send_question(message)


async def send_question(message_or_callback):
    """Tasodifiy savol yuboradi."""
    q_index = random.randint(0, len(QUESTIONS) - 1)
    question = QUESTIONS[q_index]

    text = f"🧠 <b>Test savoli:</b>\n\n{question['question']}"
    keyboard = quiz_keyboard(q_index, question["options"])

    if isinstance(message_or_callback, Message):
        await message_or_callback.answer(text, reply_markup=keyboard)
    elif isinstance(message_or_callback, CallbackQuery):
        await message_or_callback.message.answer(text, reply_markup=keyboard)


@router.callback_query(F.data.startswith("quiz:"))
async def quiz_answer(callback: CallbackQuery):
    """Test javobini tekshiradi."""
    parts = callback.data.split(":")
    q_index = int(parts[1])
    answer_index = int(parts[2])

    question = QUESTIONS[q_index]
    correct_index = question["correct"]
    correct_answer = question["options"][correct_index]

    if answer_index == correct_index:
        add_correct_answer(callback.from_user.id)
        text = (
            f"✅ <b>To'g'ri!</b> Barakalla! 🎉\n\n"
            f"Javob: <b>{correct_answer}</b>"
        )
    else:
        add_wrong_answer(callback.from_user.id)
        user_answer = question["options"][answer_index]
        text = (
            f"❌ <b>Noto'g'ri!</b>\n\n"
            f"Sizning javobingiz: {user_answer}\n"
            f"To'g'ri javob: <b>{correct_answer}</b>"
        )

    await callback.message.edit_text(text, reply_markup=quiz_next_keyboard())
    await callback.answer()


@router.callback_query(F.data == "quiz_next")
async def quiz_next(callback: CallbackQuery):
    """Keyingi savolga o'tadi."""
    await callback.answer()
    await send_question(callback)


@router.callback_query(F.data == "quiz_stats")
async def quiz_show_stats(callback: CallbackQuery):
    """Test natijalarini ko'rsatadi."""
    text = get_stats_text(callback.from_user.id)
    await callback.message.answer(text)
    await callback.answer()
