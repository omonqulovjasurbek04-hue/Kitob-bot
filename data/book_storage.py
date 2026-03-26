import json
import os

LIBRARY_FILE = os.path.join(os.path.dirname(__file__), "books_library.json")
PDF_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pdf")


def _load_library() -> dict:
    """Kitoblar kutubxonasini JSON dan o'qiydi."""
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"books": []}
    return {"books": []}


def _save_library(data: dict):
    """Kutubxonani JSON faylga yozadi."""
    with open(LIBRARY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_all_books() -> list[dict]:
    """Barcha kitoblar ro'yxatini qaytaradi."""
    data = _load_library()
    return data.get("books", [])


def get_book_by_id(book_id: int) -> dict | None:
    """ID bo'yicha kitobni topadi."""
    books = get_all_books()
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def get_pdf_path(book: dict) -> str | None:
    """Kitob PDF faylining to'liq yo'lini qaytaradi. Fayl mavjud bo'lmasa None."""
    pdf_file = book.get("pdf_file")
    if not pdf_file:
        return None
    full_path = os.path.join(PDF_DIR, pdf_file)
    if os.path.exists(full_path):
        return full_path
    return None


def add_book(title: str, author: str, short_name: str, pdf_filename: str | None = None) -> dict:
    """Yangi kitob qo'shadi."""
    from datetime import datetime
    data = _load_library()
    books = data.get("books", [])

    # Yangi ID yaratish
    max_id = max((b["id"] for b in books), default=0)
    new_id = max_id + 1

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "short_name": short_name,
        "pdf_file": pdf_filename,
        "added_date": datetime.now().strftime("%Y-%m-%d"),
    }

    books.append(new_book)
    data["books"] = books
    _save_library(data)
    return new_book


def update_book_pdf(book_id: int, pdf_filename: str) -> bool:
    """Kitobga PDF fayl nomini qo'shadi."""
    data = _load_library()
    books = data.get("books", [])
    for book in books:
        if book["id"] == book_id:
            book["pdf_file"] = pdf_filename
            _save_library(data)
            return True
    return False


def delete_book(book_id: int) -> bool:
    """Kitobni o'chiradi."""
    data = _load_library()
    books = data.get("books", [])
    original_len = len(books)
    data["books"] = [b for b in books if b["id"] != book_id]
    if len(data["books"]) < original_len:
        _save_library(data)
        return True
    return False


def ensure_pdf_dir():
    """PDF papkasi mavjudligini ta'minlaydi."""
    os.makedirs(PDF_DIR, exist_ok=True)
