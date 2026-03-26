from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def main_keyboard() -> ReplyKeyboardMarkup:
    """Asosiy menyu tugmalari."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Kitoblar"), KeyboardButton(text="🧠 Iqtibos")],
            [KeyboardButton(text="⏳ O'qishni boshlash"), KeyboardButton(text="⏹ O'qishni to'xtatish")],
            [KeyboardButton(text="📊 Statistikam"), KeyboardButton(text="❓ Test")],
            [KeyboardButton(text="💪 Motivatsiya"), KeyboardButton(text="ℹ️ Yordam")],
        ],
        resize_keyboard=True,
    )


def books_pagination_keyboard(page: int, total_pages: int) -> InlineKeyboardMarkup | None:
    """Kitoblar sahifalash tugmalari."""
    buttons = []
    if page > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"books_page:{page - 1}"))
    if page < total_pages - 1:
        buttons.append(InlineKeyboardButton(text="Keyingi ➡️", callback_data=f"books_page:{page + 1}"))

    if not buttons:
        return None

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


def quiz_keyboard(question_index: int, options: list[str]) -> InlineKeyboardMarkup:
    """Test savoli uchun inline tugmalar."""
    buttons = []
    labels = ["A", "B", "C", "D"]
    for i, option in enumerate(options):
        buttons.append([
            InlineKeyboardButton(
                text=f"{labels[i]}) {option}",
                callback_data=f"quiz:{question_index}:{i}"
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def quiz_next_keyboard() -> InlineKeyboardMarkup:
    """Keyingi savol tugmasi."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📝 Keyingi savol", callback_data="quiz_next")],
            [InlineKeyboardButton(text="📊 Natijalarim", callback_data="quiz_stats")],
        ]
    )


def book_select_keyboard(books: list[dict]) -> InlineKeyboardMarkup:
    """Kitob tanlash uchun inline tugmalar."""
    buttons = []
    for book in books:
        has_pdf = "📗" if book.get("pdf_file") else "📕"
        buttons.append([
            InlineKeyboardButton(
                text=f"{has_pdf} {book['title']} — {book['author']}",
                callback_data=f"select_book:{book['id']}"
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def admin_book_keyboard(book_id: int) -> InlineKeyboardMarkup:
    """Admin uchun kitob boshqarish tugmalari."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🗑 O'chirish", callback_data=f"admin_del_book:{book_id}")],
        ]
    )


def admin_menu_keyboard() -> InlineKeyboardMarkup:
    """Admin panel asosiy menyu tugmalari."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📖 Kitob qo'shish", callback_data="admin_add_book"),
                InlineKeyboardButton(text="📋 Kitoblar", callback_data="admin_books_list"),
            ],
            [
                InlineKeyboardButton(text="🔄 Yangilash", callback_data="admin_refresh"),
                InlineKeyboardButton(text="🚪 Chiqish", callback_data="admin_logout"),
            ],
        ]
    )
