from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from data.quotes import get_random_motivation

router = Router()


@router.message(Command("kundalik"))
async def daily_reminder(message: Message):
    """Kundalik eslatma buyrug'i."""
    motivation = get_random_motivation()
    text = (
        "🌅 <b>Kundalik eslatma!</b>\n\n"
        f"{motivation}\n\n"
        "📖 Bugun nima o'qimoqchisiz?\n"
        "⏳ <b>O'qishni boshlash</b> tugmasini bosing!"
    )
    await message.answer(text)


@router.message(F.text)
async def unknown_message(message: Message):
    """Noma'lum xabarlarni qayta ishlaydi."""
    await message.answer(
        "🤔 Kechirasiz, bu buyruqni tushunmadim.\n\n"
        "Quyidagi tugmalardan birini tanlang yoki\n"
        "/help buyrug'ini yuboring."
    )
