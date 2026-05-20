from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


# Команда /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать!\n"
        "Выберите команду."
    )


# Команда /help
@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/info\n"
        "/news\n"
        "/contacts"
    )


# Команда /info
@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer(
        "Информация о сервисе..."
    )