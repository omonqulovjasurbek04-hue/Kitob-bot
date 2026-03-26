from aiogram import Router, F
from aiogram.types import Message

from data.quotes import get_random_quote, get_random_motivation

router = Router()


@router.message(F.text == "🧠 Iqtibos")
async def show_quote(message: Message):
    """Tasodifiy iqtibos yuboradi."""
    quote = get_random_quote()
    await message.answer(quote)


@router.message(F.text == "💪 Motivatsiya")
async def show_motivation(message: Message):
    """Tasodifiy motivatsion xabar yuboradi."""
    motivation = get_random_motivation()
    await message.answer(motivation)
