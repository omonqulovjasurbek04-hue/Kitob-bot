import os

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from data.book_storage import (
    get_all_books, add_book, delete_book,
    get_book_by_id, ensure_pdf_dir, PDF_DIR
)
from keyboards.keyboards import admin_book_keyboard, admin_menu_keyboard

router = Router()

# Admin paroli
ADMIN_PASSWORD = "123456789"

# Login bo'lgan adminlar (user_id lari saqlanadi)
_logged_in_admins: set[int] = set()


class AdminStates(StatesGroup):
    waiting_password = State()
    waiting_book_title = State()
    waiting_book_author = State()
    waiting_book_short_name = State()
    waiting_book_pdf = State()


def is_admin(user_id: int) -> bool:
    """Foydalanuvchi login bo'lganligini tekshiradi."""
    return user_id in _logged_in_admins


def _build_admin_text() -> str:
    """Admin panel matnini yaratadi (takrorlanmaslik uchun)."""
    books = get_all_books()
    text = "🔧 <b>Admin Panel</b>\n\n"

    if books:
        text += f"📚 <b>Kutubxona:</b> {len(books)} ta kitob\n\n"
        for book in books:
            pdf_icon = "✅" if book.get("pdf_file") else "❌"
            text += (
                f"  <b>{book['id']}.</b> {book['title']}\n"
                f"      ✍️ {book['author']} | {pdf_icon} PDF\n"
            )
        text += "\n"
    else:
        text += "📭 Kutubxona bo'sh.\n\n"

    return text


# ─── LOGIN ────────────────────────────────────────────

@router.message(Command("admin"))
async def cmd_admin(message: Message, state: FSMContext):
    """Admin panelga kirish — parol so'raydi."""
    if is_admin(message.from_user.id):
        await message.answer(
            _build_admin_text(),
            reply_markup=admin_menu_keyboard()
        )
        return

    await state.set_state(AdminStates.waiting_password)
    await message.answer(
        "🔐 <b>Admin Panel</b>\n\n"
        "Parolni kiriting:"
    )


@router.message(AdminStates.waiting_password)
async def process_password(message: Message, state: FSMContext):
    """Parolni tekshiradi."""
    try:
        await message.delete()
    except Exception:
        pass

    if message.text == ADMIN_PASSWORD:
        _logged_in_admins.add(message.from_user.id)
        await state.clear()
        await message.answer(
            "✅ <b>Admin sifatida kirdingiz!</b>\n\n" + _build_admin_text(),
            reply_markup=admin_menu_keyboard()
        )
    else:
        await state.clear()
        await message.answer("❌ Parol noto'g'ri!")


# ─── ADMIN MENU CALLBACKS ────────────────────────────

@router.callback_query(F.data == "admin_add_book")
async def cb_add_book(callback: CallbackQuery, state: FSMContext):
    """Inline tugma orqali kitob qo'shish."""
    if not is_admin(callback.from_user.id):
        await callback.answer("⛔ Admin emassiz!", show_alert=True)
        return

    await state.set_state(AdminStates.waiting_book_title)
    await callback.message.answer(
        "📖 <b>Yangi kitob qo'shish</b>\n\n"
        "Kitob nomini kiriting:"
    )
    await callback.answer()


@router.callback_query(F.data == "admin_books_list")
async def cb_books_list(callback: CallbackQuery):
    """Kitoblar ro'yxatini o'chirish tugmalari bilan ko'rsatadi."""
    if not is_admin(callback.from_user.id):
        await callback.answer("⛔ Admin emassiz!", show_alert=True)
        return

    books = get_all_books()
    if not books:
        await callback.answer("📭 Kutubxona bo'sh!", show_alert=True)
        return

    for book in books:
        pdf_icon = "✅ PDF" if book.get("pdf_file") else "❌ PDFsiz"
        await callback.message.answer(
            f"📖 <b>{book['title']}</b>\n"
            f"✍️ {book['author']} | {pdf_icon}",
            reply_markup=admin_book_keyboard(book["id"]),
        )
    await callback.answer()


@router.callback_query(F.data == "admin_logout")
async def cb_logout(callback: CallbackQuery):
    """Admindan chiqish."""
    _logged_in_admins.discard(callback.from_user.id)
    await callback.message.edit_text("🔓 Admin paneldan chiqdingiz.")
    await callback.answer()


@router.callback_query(F.data == "admin_refresh")
async def cb_refresh(callback: CallbackQuery):
    """Admin panelni yangilash."""
    if not is_admin(callback.from_user.id):
        await callback.answer("⛔ Admin emassiz!", show_alert=True)
        return

    await callback.message.edit_text(
        _build_admin_text(),
        reply_markup=admin_menu_keyboard()
    )
    await callback.answer("🔄 Yangilandi!")


# ─── KITOB QO'SHISH (FSM) ────────────────────────────

@router.message(Command("add_book"))
async def cmd_add_book(message: Message, state: FSMContext):
    """Buyruq orqali kitob qo'shish."""
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Avval /admin orqali kiring!")
        return

    await state.set_state(AdminStates.waiting_book_title)
    await message.answer(
        "📖 <b>Yangi kitob qo'shish</b>\n\n"
        "Kitob nomini kiriting:"
    )


@router.message(AdminStates.waiting_book_title)
async def process_book_title(message: Message, state: FSMContext):
    """Kitob nomi kiritildi."""
    await state.update_data(title=message.text)
    await state.set_state(AdminStates.waiting_book_author)
    await message.answer(
        f"📖 Kitob: <b>{message.text}</b>\n\n"
        "Muallif ismini kiriting:"
    )


@router.message(AdminStates.waiting_book_author)
async def process_book_author(message: Message, state: FSMContext):
    """Muallif nomi kiritildi."""
    await state.update_data(author=message.text)
    await state.set_state(AdminStates.waiting_book_short_name)
    await message.answer(
        f"✍️ Muallif: <b>{message.text}</b>\n\n"
        "Kitobning qisqacha nomini kiriting\n"
        "(masalan: <code>odam_bolish_qiyin</code>):"
    )


@router.message(AdminStates.waiting_book_short_name)
async def process_book_short_name(message: Message, state: FSMContext):
    """Qisqacha nom kiritildi."""
    short_name = message.text.strip().lower().replace(" ", "_")
    await state.update_data(short_name=short_name)
    await state.set_state(AdminStates.waiting_book_pdf)
    await message.answer(
        f"📂 Qisqacha nom: <code>{short_name}</code>\n\n"
        "Endi PDF faylni yuboring 📤\n\n"
        "Yoki /skip — PDFsiz saqlash"
    )


@router.message(AdminStates.waiting_book_pdf, Command("skip"))
async def skip_pdf(message: Message, state: FSMContext):
    """PDF yubormasdan saqlash."""
    data = await state.get_data()
    new_book = add_book(
        title=data["title"],
        author=data["author"],
        short_name=data["short_name"],
        pdf_filename=None
    )
    await state.clear()
    await message.answer(
        f"✅ <b>Kitob saqlandi!</b>\n\n"
        f"📖 {new_book['title']}\n"
        f"✍️ {new_book['author']}\n"
        "❌ PDF hali qo'shilmagan"
    )


@router.message(AdminStates.waiting_book_pdf, F.document)
async def process_book_pdf(message: Message, state: FSMContext, bot: Bot):
    """PDF fayl yuborildi."""
    document = message.document

    if not document.file_name.lower().endswith(".pdf"):
        await message.answer("❌ Faqat PDF fayl yuboring!")
        return

    data = await state.get_data()
    ensure_pdf_dir()

    pdf_filename = document.file_name
    pdf_path = os.path.join(PDF_DIR, pdf_filename)

    file = await bot.get_file(document.file_id)
    await bot.download_file(file.file_path, destination=pdf_path)

    new_book = add_book(
        title=data["title"],
        author=data["author"],
        short_name=data["short_name"],
        pdf_filename=pdf_filename
    )

    await state.clear()
    await message.answer(
        f"✅ <b>Kitob saqlandi!</b>\n\n"
        f"📖 {new_book['title']}\n"
        f"✍️ {new_book['author']}\n"
        f"✅ PDF: {pdf_filename}\n\n"
        "🎉 Kutubxonaga qo'shildi!"
    )


@router.message(AdminStates.waiting_book_pdf)
async def invalid_pdf(message: Message):
    """Noto'g'ri fayl yuborildi."""
    await message.answer(
        "❌ PDF fayl yuboring yoki /skip buyrug'ini kiriting."
    )


# ─── KITOB O'CHIRISH ─────────────────────────────────

@router.callback_query(F.data.startswith("admin_del_book:"))
async def admin_delete_book(callback: CallbackQuery):
    """Kitobni o'chiradi."""
    if not is_admin(callback.from_user.id):
        await callback.answer("⛔ Admin emassiz!", show_alert=True)
        return

    book_id = int(callback.data.split(":")[1])
    book = get_book_by_id(book_id)

    if book and delete_book(book_id):
        await callback.message.edit_text(
            f"🗑 <b>{book['title']}</b> o'chirildi!"
        )
    else:
        await callback.message.edit_text("❌ Kitob topilmadi!")
    await callback.answer()
