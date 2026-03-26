import random

# O'zbek adabiyotidan va jahon donishmandlaridan iqtiboslar
QUOTES = [
    "📖 Kitob — insonning eng yaqin do'sti. — Abdulla Avloniy",
    "📖 O'qish — eng yaxshi sarmoya. — Benjamin Franklin",
    "📖 Kitob o'qigan odam hech qachon yolg'iz bo'lmaydi.",
    "📖 Bilim — bu kuch. — Frensis Bekon",
    "📖 O'qish — ruhning oziqlanishi. — Siseron",
    "📖 Yaxshi kitob — eng yaxshi do'st. — Angliya maqoli",
    "📖 Kitobsiz hayot — quyoshsiz kabi. — Abdulla Avloniy",
    "📖 Ozod fikr — ozod kitob orqali keladi.",
    "📖 Kitob — kelajakka yo'l ochuvchi kalit.",
    "📖 O'qimaydigan inson — ko'r inson. — Xalq maqoli",
    "📖 Har kuni bir sahifa o'qi, bir yilda 365 sahifa o'qigan bo'lasan.",
    "📖 Bilimli bo'lish uchun ko'p o'qish kerak. — Alisher Navoiy",
    "📖 Donishmandlik — kitob sahifalarida yashiringan.",
    "📖 So'z — kumush, jim turish — oltin. Lekin kitob — olmos.",
    "📖 Eng kuchli qurol — bilim va kitob. — Nelson Mandela",
    "📖 O'qish — boshqa olamga sayohat qilish demak.",
    "📖 Kitob — o'tmish va kelajak o'rtasidagi ko'prik.",
    "📖 O'qigan kishi — dunyoni yutadi.",
    "📖 Aql — kitobning eng yaxshi merosxo'ri.",
    "📖 Har bir kitob — yangi bir ufq ochadi.",
    "📖 Bilim daraxti — kitob bilan sug'oriladi.",
    "📖 Mutolaa — aql uchun mashq, ruh uchun oziq.",
    "📖 Yuz marta eshitgandan, bir marta o'qigan yaxshi.",
    "📖 Kitob o'qish — o'zingni topish yo'li.",
    "📖 Eng boy odam — eng ko'p kitob o'qigan odam.",
]


# Motivatsion xabarlar
MOTIVATIONS = [
    "💪 Bugun ham o'qishni unutmang!",
    "🌟 Har kuni 15 minut o'qish hayotingizni o'zgartiradi!",
    "🎯 Maqsadga kitob bilan yetishing!",
    "🔥 O'qish — eng yaxshi investitsiya!",
    "⭐ Bugungi o'qishingiz — ertangi yutuqingiz!",
    "📚 Bir kitob tugatdingizmi? Yangi birini boshlang!",
    "🧠 Miyangizni mashq qiltiramiz — o'qiymiz!",
    "🌈 O'qi, o'rgan, o'zgar!",
]


def get_random_quote() -> str:
    """Tasodifiy iqtibos qaytaradi."""
    return random.choice(QUOTES)


def get_random_motivation() -> str:
    """Tasodifiy motivatsion xabar qaytaradi."""
    return random.choice(MOTIVATIONS)
