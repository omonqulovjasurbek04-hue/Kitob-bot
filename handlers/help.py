from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from data.books import get_total_books
from data.questions import get_total_questions

router = Router()


@router.message(Command("help"))
@router.message(F.text == "ℹ️ Yordam")
async def show_help(message: Message):
    """Bot haqida ma'lumot va yordam."""
    text = (
        "ℹ️ <b>Mutolaa Bot — Yordam</b>\n\n"
        "Bu bot sizga kitob o'qish odatingizni\n"
        "shakllantirish va bilimingizni oshirishda\n"
        "yordam beradi.\n\n"
        "<b>📚 Kitoblar</b>\n"
        f"  └ {get_total_books()} ta eng yaxshi kitoblar ro'yxati\n"
        "  └ Har bir kitob haqida ma'lumot\n"
        "  └ Sahifalash bilan qulay ko'rish\n\n"
        "<b>🧠 Iqtibos</b>\n"
        "  └ Tasodifiy foydali iqtiboslar\n"
        "  └ Har safar yangi iqtibos\n\n"
        "<b>⏳ O'qishni boshlash / ⏹ To'xtatish</b>\n"
        "  └ O'qish vaqtingizni kuzatish\n"
        "  └ Sessiyalar soni va jami vaqt\n\n"
        "<b>📊 Statistikam</b>\n"
        "  └ Jami o'qish vaqtingiz\n"
        "  └ Test natijalari va aniqlik foizi\n\n"
        "<b>❓ Test</b>\n"
        f"  └ {get_total_questions()} ta savol (o'zbek adabiyoti)\n"
        "  └ 4 variantli inline tugmalar\n"
        "  └ Natijalar avtomatik saqlanadi\n\n"
        "<b>💪 Motivatsiya</b>\n"
        "  └ Ruhlantiruvchi xabarlar\n\n"
        "📌 <b>Buyruqlar:</b>\n"
        "  /start — Botni qayta ishga tushirish\n"
        "  /help — Yordam"
    )
    await message.answer(text)
