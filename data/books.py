# O'zbek adabiyoti va jahon adabiyoti kitoblari

BOOKS = [
    {
        "title": "📕 O'tkan kunlar",
        "author": "Abdulla Qodiriy",
        "year": 1926,
        "genre": "Roman",
        "desc": "O'zbek adabiyotining birinchi romani. Otabek va Kumushning sevgi va fojia to'la qismati."
    },
    {
        "title": "📗 Mehrobdan chayon",
        "author": "Abdulhamid Cho'lpon",
        "year": 1929,
        "genre": "Roman",
        "desc": "Turkiston hayoti va xalq ozodligi haqidagi chuqur asar."
    },
    {
        "title": "📘 Sariq devni minib",
        "author": "Xudoyberdi To'xtaboyev",
        "year": 1962,
        "genre": "Bolalar adabiyoti",
        "desc": "Bolalar sarguzashtlari haqidagi qiziqarli qissa."
    },
    {
        "title": "📙 Kecha va kunduz",
        "author": "Cho'lpon",
        "year": 1936,
        "genre": "Roman",
        "desc": "Zebi ismli qizning hayoti va o'sha davr jamiyati tasvirlangan."
    },
    {
        "title": "📕 Shum bola",
        "author": "G'afur G'ulom",
        "year": 1936,
        "genre": "Qissa",
        "desc": "Yosh bolaning hajviy va qiziqarli sarguzashtlari."
    },
    {
        "title": "📗 Navoi",
        "author": "Oybek",
        "year": 1945,
        "genre": "Tarixiy roman",
        "desc": "Buyuk shoir Alisher Navoiyning hayoti va ijodi."
    },
    {
        "title": "📘 Oltin yulduz",
        "author": "To'xtasin Jalolov",
        "year": 1983,
        "genre": "Detektiv",
        "desc": "O'zbek detektiv janridagi mashhur asar."
    },
    {
        "title": "📙 Kelajak evaziga",
        "author": "Pirimqul Qodirov",
        "year": 1968,
        "genre": "Roman",
        "desc": "Yosh avlodning kelajak uchun kurashini tasvirlovchi asar."
    },
    {
        "title": "📕 Ufq",
        "author": "Said Ahmad",
        "year": 1970,
        "genre": "Roman",
        "desc": "O'zbek qishloq hayoti va o'zgarishlar haqida."
    },
    {
        "title": "📗 Yulduzli tunlar",
        "author": "Pirimqul Qodirov",
        "year": 1978,
        "genre": "Tarixiy roman",
        "desc": "Bobur Mirzoning hayoti va sarguzashtlari."
    },
    {
        "title": "📘 Bahor qaytmaydi",
        "author": "Hamid Olimjon",
        "year": 1940,
        "genre": "Dramaturglik",
        "desc": "Sevgi, vatan va fidoyilik haqidagi asar."
    },
    {
        "title": "📙 Ko'hna dunyo",
        "author": "Abdulla Qahhor",
        "year": 1951,
        "genre": "Roman",
        "desc": "Eski jamiyat va yangi davr o'rtasidagi ziddiyat."
    },
    {
        "title": "📕 Kichkina shahzoda",
        "author": "Antuan de Sent-Ekzyuperi",
        "year": 1943,
        "genre": "Ertak-falsafa",
        "desc": "Yoshlar va kattalar uchun falsafiy ertak. Ingliz tilidan tarjima."
    },
    {
        "title": "📗 Alximik",
        "author": "Paulo Koelo",
        "year": 1988,
        "genre": "Falsafiy roman",
        "desc": "Orzularni amalga oshirish va o'z yo'lini topish haqida."
    },
    {
        "title": "📘 1984",
        "author": "Jorj Oruell",
        "year": 1949,
        "genre": "Distopiya",
        "desc": "Totalitar jamiyat va shaxs erkinligi haqida."
    },
]


def get_books_text(page: int = 0, per_page: int = 5) -> tuple[str, int]:
    """Kitoblar ro'yxatini sahifalab qaytaradi."""
    total_pages = (len(BOOKS) + per_page - 1) // per_page
    page = max(0, min(page, total_pages - 1))
    start = page * per_page
    end = start + per_page
    books_slice = BOOKS[start:end]

    text = f"📚 <b>Kitoblar ro'yxati</b> (sahifa {page + 1}/{total_pages}):\n\n"
    for i, book in enumerate(books_slice, start=start + 1):
        text += (
            f"<b>{i}. {book['title']}</b>\n"
            f"    ✍️ {book['author']} ({book['year']})\n"
            f"    📂 Janr: {book['genre']}\n"
            f"    📝 {book['desc']}\n\n"
        )

    return text, total_pages


def get_total_books() -> int:
    return len(BOOKS)
