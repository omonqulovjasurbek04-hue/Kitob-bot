from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboards import main_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Bot ishga tushganda yuboriladigan xabar."""
    text = (
        "👋 <b>Salom, {name}!</b>\n\n"
        "📖 <b>Mutolaa Bot</b>ga xush kelibsiz!\n\n"
        "Bu bot sizga:\n"
        "📚 Eng yaxshi kitoblarni tavsiya qiladi\n"
        "🧠 Foydali iqtiboslar beradi\n"
        "⏱ O'qish vaqtingizni kuzatadi\n"
        "❓ Bilimingizni test qiladi\n"
        "📊 Statistikangizni ko'rsatadi\n\n"
        "Quyidagi tugmalardan birini tanlang 👇"
    ).format(name=message.from_user.first_name)

    await message.answer(text, reply_markup=main_keyboard())
