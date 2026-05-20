import os
import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message


TOKEN = os.getenv("TELEGRAM_TOKEN")

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать!\n"
        "Выберите команду."
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/info\n"
        "/news\n"
        "/contacts"
    )


@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer(
        "Информация о сервисе..."
    )


@router.message(Command("news"))
async def cmd_news(message: Message):
    await message.answer(
        "Новости сервиса:\n"
        "На данный момент новых уведомлений нет."
    )


@router.message(Command("contacts"))
async def cmd_contacts(message: Message):
    await message.answer(
        "Контакты:\n"
        "example@mail.ru"
    )


async def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN не найден. Добавьте переменную окружения TELEGRAM_TOKEN.")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())