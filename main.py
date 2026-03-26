import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

# Handlerlarni import qilish
from handlers import start, books, quotes, reading, stats, test, help, daily, admin

load_dotenv()
API_TOKEN = os.getenv("API")

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


async def main():
    """Botni ishga tushiradi."""
    bot = Bot(
        token=API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Barcha routerlarni ro'yxatdan o'tkazish
    dp.include_routers(
        start.router,
        admin.router,   # admin — FSM stateli, daily dan oldin bo'lishi kerak
        books.router,
        quotes.router,
        reading.router,
        stats.router,
        test.router,
        help.router,
        daily.router,   # daily eng oxirida — unknown_message fallback shu yerda
    )

    logging.info("Bot ishga tushdi!")

    # Polling boshlash
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())