from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from data.books import get_books_text
from keyboards.keyboards import books_pagination_keyboard

router = Router()


@router.message(F.text == "📚 Kitoblar")
async def show_books(message: Message):
    """Kitoblar ro'yxatining birinchi sahifasini ko'rsatadi."""
    text, total_pages = get_books_text(page=0)
    keyboard = books_pagination_keyboard(0, total_pages)
    await message.answer(text, reply_markup=keyboard)


@router.callback_query(F.data.startswith("books_page:"))
async def books_page_callback(callback: CallbackQuery):
    """Kitoblar sahifalash callback."""
    page = int(callback.data.split(":")[1])
    text, total_pages = get_books_text(page=page)
    keyboard = books_pagination_keyboard(page, total_pages)
    await callback.message.edit_text(text, reply_markup=keyboard)
    await callback.answer()
