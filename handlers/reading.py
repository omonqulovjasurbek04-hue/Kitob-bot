from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile

from data.book_storage import get_all_books, get_book_by_id, get_pdf_path
from keyboards.keyboards import book_select_keyboard
from utils.storage import start_reading, stop_reading, is_reading, get_reading_duration

router = Router()


@router.message(F.text == "⏳ O'qishni boshlash")
async def cmd_start_reading(message: Message):
    """O'qishni boshlash — avval kitob tanlash."""
    user_id = message.from_user.id

    if is_reading(user_id):
        minutes = get_reading_duration(user_id)
        await message.answer(
            f"⚠️ Siz allaqachon o'qiyapsiz!\n"
            f"⏱ Hozirgi sessiya: <b>{minutes} minut</b>\n\n"
            f"Tugatish uchun <b>⏹ O'qishni to'xtatish</b> tugmasini bosing."
        )
        return

    books = get_all_books()
    if not books:
        await message.answer(
            "📭 Hozircha kutubxonada kitob yo'q.\n\n"
            "Admin tez orada kitoblar qo'shadi!"
        )
        return

    keyboard = book_select_keyboard(books)
    await message.answer(
        "📚 <b>Kitob tanlang:</b>\n\n"
        "📗 — PDF mavjud\n"
        "📕 — PDF hali qo'shilmagan\n\n"
        "O'qimoqchi bo'lgan kitobni tanlang 👇",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("select_book:"))
async def book_selected(callback: CallbackQuery, bot: Bot):
    """Kitob tanlanganda PDF yuboradi va o'qishni boshlaydi."""
    book_id = int(callback.data.split(":")[1])
    book = get_book_by_id(book_id)

    if not book:
        await callback.answer("❌ Kitob topilmadi!", show_alert=True)
        return

    pdf_path = get_pdf_path(book)

    if not pdf_path:
        await callback.message.edit_text(
            f"📕 <b>{book['title']}</b>\n"
            f"✍️ {book['author']}\n\n"
            f"❌ Admin hali bu kitobning PDF faylini qo'shmagan.\n"
            f"Tez orada qo'shiladi! 📩"
        )
        await callback.answer()
        return

    # O'qishni boshlash
    start_reading(callback.from_user.id)

    await callback.message.edit_text(
        f"📗 <b>{book['title']}</b>\n"
        f"✍️ {book['author']}\n\n"
        f"⏱ <b>O'qish boshlandi!</b>\n"
        f"PDF yuborilmoqda... 📤"
    )

    # PDF faylni yuborish
    pdf_file = FSInputFile(pdf_path, filename=f"{book['title']}.pdf")
    await bot.send_document(
        chat_id=callback.from_user.id,
        document=pdf_file,
        caption=(
            f"📖 <b>{book['title']}</b>\n"
            f"✍️ {book['author']}\n\n"
            f"Yoqimli mutolaa! 📚\n"
            f"Tugatgach <b>⏹ O'qishni to'xtatish</b> tugmasini bosing."
        )
    )
    await callback.answer()


@router.message(F.text == "⏹ O'qishni to'xtatish")
async def cmd_stop_reading(message: Message):
    """O'qishni to'xtatadi."""
    user_id = message.from_user.id

    if not is_reading(user_id):
        await message.answer(
            "❗ Siz hali o'qishni boshlamagansiz.\n\n"
            "<b>⏳ O'qishni boshlash</b> tugmasini bosing."
        )
        return

    minutes = stop_reading(user_id)
    if minutes is not None:
        if minutes < 1:
            time_text = "1 minutdan kam"
        elif minutes < 60:
            time_text = f"{minutes} minut"
        else:
            hours = minutes // 60
            remaining = minutes % 60
            time_text = f"{hours} soat {remaining} minut"

        await message.answer(
            f"✅ <b>O'qish tugatildi!</b>\n\n"
            f"⏱ Bu sessiyada siz <b>{time_text}</b> o'qidingiz!\n\n"
            f"👏 Zo'r! Davom eting!"
        )
    else:
        await message.answer(
            "⚠️ O'qish sessiyasi topilmadi.\n"
            "<b>⏳ O'qishni boshlash</b> tugmasini bosing."
        )
