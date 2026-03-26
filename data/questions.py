# O'zbek adabiyoti bo'yicha test savollari
QUESTIONS = [
    {
        "question": "📖 'O'tkan kunlar' romani muallifi kim?",
        "options": ["Abdulla Qodiriy", "Cho'lpon", "Oybek", "G'afur G'ulom"],
        "correct": 0
    },
    {
        "question": "📖 'Mehrobdan chayon' romani muallifi kim?",
        "options": ["Pirimqul Qodirov", "Abdulhamid Cho'lpon", "Abdulla Qahhor", "Said Ahmad"],
        "correct": 1
    },
    {
        "question": "📖 'Yulduzli tunlar' romani qaysi tarixiy shaxs haqida?",
        "options": ["Amir Temur", "Alisher Navoiy", "Zahiriddin Bobur", "Jaloliddin Manguberdi"],
        "correct": 2
    },
    {
        "question": "📖 'Navoi' romanining muallifi kim?",
        "options": ["Hamid Olimjon", "Oybek", "Mirtemir", "Zulfiya"],
        "correct": 1
    },
    {
        "question": "📖 'Shum bola' qissasini kim yozgan?",
        "options": ["Abdulla Qahhor", "Pirimqul Qodirov", "G'afur G'ulom", "Hamza"],
        "correct": 2
    },
    {
        "question": "📖 O'zbek tilining birinchi romani qaysi?",
        "options": ["Kecha va kunduz", "O'tkan kunlar", "Mehrobdan chayon", "Navoi"],
        "correct": 1
    },
    {
        "question": "📖 'Sariq devni minib' qissasi muallifi kim?",
        "options": ["Xudoyberdi To'xtaboyev", "G'afur G'ulom", "Hamid Olimjon", "Said Ahmad"],
        "correct": 0
    },
    {
        "question": "📖 'Kecha va kunduz' romani qahramoni qaysi?",
        "options": ["Kumush", "Gulnor", "Zebi", "Nodira"],
        "correct": 2
    },
    {
        "question": "📖 Alisher Navoiy qaysi asrda yashagan?",
        "options": ["XIII asr", "XIV asr", "XV asr", "XVI asr"],
        "correct": 2
    },
    {
        "question": "📖 'Xamsa' asarining muallifi kim?",
        "options": ["Bobur", "Navoiy", "Lutfiy", "Mashrab"],
        "correct": 1
    },
    {
        "question": "📖 'Boburnoma' qanday janrdagi asar?",
        "options": ["Roman", "Doston", "Memuar (xotira)", "Hikoya"],
        "correct": 2
    },
    {
        "question": "📖 O'zbek adabiyotida 'Jadidchilik' harakati qachon boshlangan?",
        "options": ["XVIII asr oxiri", "XIX asr boshi", "XX asr boshi", "XVII asr"],
        "correct": 2
    },
    {
        "question": "📖 'Lolazor' dostonini kim yozgan?",
        "options": ["Erkin Vohidov", "Abdulla Oripov", "Rauf Parfi", "Hamid Olimjon"],
        "correct": 0
    },
    {
        "question": "📖 'O'zbegim' she'rining muallifi kim?",
        "options": ["Erkin Vohidov", "Abdulla Oripov", "Muhammad Yusuf", "Rauf Parfi"],
        "correct": 1
    },
    {
        "question": "📖 Qaysi asar Amir Temur haqida yozilgan?",
        "options": ["Yulduzli tunlar", "Ko'hna dunyo", "So'ngi kunlar", "Ulug'bek xazinasi"],
        "correct": 3
    },
]


def get_total_questions() -> int:
    """Umumiy savollar sonini qaytaradi."""
    return len(QUESTIONS)
