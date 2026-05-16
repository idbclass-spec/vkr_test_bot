import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог"), KeyboardButton(text="Помощь")],
        [KeyboardButton(text="Контакты"), KeyboardButton(text="О боте")]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\nВыберите действие:",
        reply_markup=menu
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Доступные команды:\n/start\n/help")


@dp.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer("Раздел каталога: список товаров или услуг.")


@dp.message(F.text == "Помощь")
async def help_button(message: Message):
    await message.answer("Раздел помощи: выберите интересующий вопрос.")


@dp.message(F.text == "Контакты")
async def contacts(message: Message):
    await message.answer("Контакты: example@mail.ru")


@dp.message(F.text == "О боте")
async def about(message: Message):
    await message.answer("Данный Telegram-бот демонстрирует menu-driven интерфейс.")


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())