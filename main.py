import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Bot & Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# -----------------------------
# /start
# -----------------------------
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в Информационный бот!\n\n"
        "Доступные команды:\n"
        "/news — последние новости\n"
        "/world — мировые новости\n"
        "/tech — технологии\n"
        "/sport — спорт\n"
        "/help — помощь\n"
        "/about — о боте"
    )

# -----------------------------
# /help
# -----------------------------
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📖 Как пользоваться ботом:\n\n"
        "/news — показать последние новости\n"
        "/world — мировые новости\n"
        "/tech — новости технологий\n"
        "/sport — спортивные новости\n"
        "/about — информация о боте"
    )

# -----------------------------
# /news
# -----------------------------
@dp.message(Command("news"))
async def cmd_news(message: Message):
    await message.answer(
        "📰 Последние новости:\n\n"
        "🌍 ООН провела экстренное заседание по климату.\n"
        "💻 Выпущена новая версия Python 3.14.\n"
        "⚽ Чемпион мира по футболу определится в финале."
    )

# -----------------------------
# /world
# -----------------------------
@dp.message(Command("world"))
async def cmd_world(message: Message):
    await message.answer(
        "🌍 Мировые новости:\n\n"
        "• ООН провела экстренное заседание по климату.\n"
        "• Лидеры G7 договорились о новых мерах сотрудничества."
    )

# -----------------------------
# /tech
# -----------------------------
@dp.message(Command("tech"))
async def cmd_tech(message: Message):
    await message.answer(
        "💻 Новости технологий:\n\n"
        "• Выпущена новая версия Python 3.14.\n"
        "• ИИ научился решать сложные математические задачи."
    )

# -----------------------------
# /sport
# -----------------------------
@dp.message(Command("sport"))
async def cmd_sport(message: Message):
    await message.answer(
        "⚽ Спортивные новости:\n\n"
        "• Чемпион мира по футболу определится в финале.\n"
        "• НБА объявила состав команды Всех звёзд."
    )

# -----------------------------
# /about
# -----------------------------
@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "ℹ️ О боте\n\n"
        "Информационный Telegram-бот.\n"
        "Архитектура: command-based.\n"
        "Язык разработки: Python + aiogram."
    )

# -----------------------------
# START BOT
# -----------------------------
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())