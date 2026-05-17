import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Каталог", callback_data="catalog"),
            InlineKeyboardButton(text="Помощь", callback_data="help")
        ],
        [
            InlineKeyboardButton(text="Контакты", callback_data="contacts"),
            InlineKeyboardButton(text="О боте", callback_data="about")
        ]
    ]
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\nВыберите действие:",
        reply_markup=menu
    )

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Доступные команды:\n/start\n/help"
    )

@dp.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.message.answer("Раздел каталога: список товаров или услуг.")
    await callback.answer()

@dp.callback_query(F.data == "help")
async def help_button(callback: CallbackQuery):
    await callback.message.answer("Раздел помощи: выберите интересующий вопрос.")
    await callback.answer()

@dp.callback_query(F.data == "contacts")
async def contacts(callback: CallbackQuery):
    await callback.message.answer("Контакты: example@mail.ru")
    await callback.answer()

@dp.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    await callback.message.answer(
        "Данный Telegram-бот демонстрирует menu-driven интерфейс."
    )
    await callback.answer()

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())