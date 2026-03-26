from aiogram import Router, F
from aiogram.types import Message

from utils.storage import get_stats_text

router = Router()


@router.message(F.text == "📊 Statistikam")
async def show_stats(message: Message):
    """Foydalanuvchi statistikasini ko'rsatadi."""
    text = get_stats_text(message.from_user.id)
    await message.answer(text)
