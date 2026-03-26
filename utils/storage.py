import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "user_data.json")


def _load_data() -> dict:
    """JSON fayldan ma'lumotlarni o'qiydi."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def _save_data(data: dict):
    """Ma'lumotlarni JSON faylga yozadi."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _ensure_user(data: dict, user_id: int) -> dict:
    """Foydalanuvchi ma'lumotlari mavjudligini ta'minlaydi. Yangi bo'lsa yaratadi."""
    uid = str(user_id)
    if uid not in data:
        data[uid] = {
            "total_minutes": 0,
            "sessions": 0,
            "correct_answers": 0,
            "wrong_answers": 0,
            "reading_start": None,
            "books_read": 0,
            "streak_days": 0,
            "last_active": None,
        }
    return data[uid]


def _get_user_data(user_id: int) -> dict:
    """Foydalanuvchi ma'lumotlarini qaytaradi."""
    data = _load_data()
    user = _ensure_user(data, user_id)
    _save_data(data)
    return user


def start_reading(user_id: int):
    """O'qishni boshlashni qayd etadi."""
    data = _load_data()
    _ensure_user(data, user_id)
    uid = str(user_id)
    data[uid]["reading_start"] = datetime.now().isoformat()
    _save_data(data)


def stop_reading(user_id: int) -> int | None:
    """O'qishni to'xtatadi va necha minut o'qilganini qaytaradi."""
    data = _load_data()
    uid = str(user_id)
    if uid not in data or data[uid].get("reading_start") is None:
        return None

    start_time = datetime.fromisoformat(data[uid]["reading_start"])
    delta = datetime.now() - start_time
    minutes = int(delta.total_seconds()) // 60  # total_seconds() — 24 soatdan oshsa ham to'g'ri ishlaydi

    data[uid]["total_minutes"] = data[uid].get("total_minutes", 0) + minutes
    data[uid]["sessions"] = data[uid].get("sessions", 0) + 1
    data[uid]["reading_start"] = None
    data[uid]["last_active"] = datetime.now().strftime("%Y-%m-%d")

    _save_data(data)
    return minutes


def is_reading(user_id: int) -> bool:
    """Foydalanuvchi hozir o'qiyaptimi tekshiradi."""
    data = _load_data()
    uid = str(user_id)
    return uid in data and data[uid].get("reading_start") is not None


def get_reading_duration(user_id: int) -> int:
    """Joriy o'qish sessiyasi davomiyligini minut sifatida qaytaradi."""
    data = _load_data()
    uid = str(user_id)
    if uid in data and data[uid].get("reading_start") is not None:
        start_time = datetime.fromisoformat(data[uid]["reading_start"])
        delta = datetime.now() - start_time
        return int(delta.total_seconds()) // 60
    return 0


def add_correct_answer(user_id: int):
    """To'g'ri javoblar sonini 1 ga oshiradi."""
    data = _load_data()
    _ensure_user(data, user_id)
    uid = str(user_id)
    data[uid]["correct_answers"] = data[uid].get("correct_answers", 0) + 1
    _save_data(data)


def add_wrong_answer(user_id: int):
    """Noto'g'ri javoblar sonini 1 ga oshiradi."""
    data = _load_data()
    _ensure_user(data, user_id)
    uid = str(user_id)
    data[uid]["wrong_answers"] = data[uid].get("wrong_answers", 0) + 1
    _save_data(data)


def get_stats(user_id: int) -> dict:
    """Foydalanuvchi statistikasini qaytaradi."""
    return _get_user_data(user_id)


def get_stats_text(user_id: int) -> str:
    """Statistikani formatlangan matn sifatida qaytaradi."""
    stats = get_stats(user_id)
    total_correct = stats.get("correct_answers", 0)
    total_wrong = stats.get("wrong_answers", 0)
    total_tests = total_correct + total_wrong
    accuracy = (total_correct / total_tests * 100) if total_tests > 0 else 0

    text = (
        "📊 <b>Sizning statistikangiz:</b>\n\n"
        f"📖 Jami o'qish vaqti: <b>{stats.get('total_minutes', 0)} minut</b>\n"
        f"🔄 O'qish sessiyalari: <b>{stats.get('sessions', 0)} marta</b>\n"
        f"✅ To'g'ri javoblar: <b>{total_correct}</b>\n"
        f"❌ Noto'g'ri javoblar: <b>{total_wrong}</b>\n"
        f"📈 Aniqlik: <b>{accuracy:.1f}%</b>\n"
    )

    if is_reading(user_id):
        current_min = get_reading_duration(user_id)
        text += f"\n⏱ Hozir o'qiyapsiz: <b>{current_min} minut</b>"

    return text
