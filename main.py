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
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


# FSM states
class Registration(StatesGroup):
    name = State()
    email = State()


# Main menu
menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Каталог",
                callback_data="catalog"
            ),
            InlineKeyboardButton(
                text="Помощь",
                callback_data="help"
            )
        ],
        [
            InlineKeyboardButton(
                text="Контакты",
                callback_data="contacts"
            ),
            InlineKeyboardButton(
                text="О боте",
                callback_data="about"
            )
        ],
        [
            InlineKeyboardButton(
                text="Регистрация",
                callback_data="register"
            )
        ]
    ]
)


# /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\n"
        "Выберите действие:",
        reply_markup=menu
    )


# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Доступные команды:\n\n"
        "/start — главное меню\n"
        "/help — помощь\n"
        "/register — регистрация пользователя\n"
        "/cancel — отмена регистрации"
    )


# /register
@dp.message(Command("register"))
async def register_start(
    message: Message,
    state: FSMContext
):
    await state.set_state(Registration.name)

    await message.answer(
        "Введите ваше имя:"
    )


# Registration button
@dp.callback_query(F.data == "register")
async def register_button(
    callback: CallbackQuery,
    state: FSMContext
):
    await state.set_state(Registration.name)

    await callback.message.answer(
        "Введите ваше имя:"
    )

    await callback.answer()


# Get name
@dp.message(Registration.name)
async def get_name(
    message: Message,
    state: FSMContext
):
    await state.update_data(
        name=message.text
    )

    await state.set_state(
        Registration.email
    )

    await message.answer(
        "Введите адрес электронной почты:"
    )


# Get email
@dp.message(Registration.email)
async def get_email(
    message: Message,
    state: FSMContext
):
    await state.update_data(
        email=message.text
    )

    data = await state.get_data()

    await message.answer(
        "Регистрация завершена.\n\n"
        f"Имя: {data['name']}\n"
        f"Email: {data['email']}"
    )

    await state.clear()


# /cancel
@dp.message(Command("cancel"))
async def cancel(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await message.answer(
        "Регистрация отменена."
    )


# Catalog button
@dp.callback_query(F.data == "catalog")
async def catalog(
    callback: CallbackQuery
):
    await callback.message.answer(
        "Раздел каталога:\n"
        "Список товаров или услуг."
    )

    await callback.answer()


# Help button
@dp.callback_query(F.data == "help")
async def help_button(
    callback: CallbackQuery
):
    await callback.message.answer(
        "Доступные команды:\n\n"
        "/start — главное меню\n"
        "/help — помощь\n"
        "/register — регистрация пользователя\n"
        "/cancel — отмена регистрации"
    )

    await callback.answer()


# Contacts button
@dp.callback_query(F.data == "contacts")
async def contacts(
    callback: CallbackQuery
):
    await callback.message.answer(
        "Контакты:\n"
        "example@mail.ru"
    )

    await callback.answer()


# About button
@dp.callback_query(F.data == "about")
async def about(
    callback: CallbackQuery
):
    await callback.message.answer(
        "Данный Telegram-бот разработан "
        "на Python с использованием "
        "библиотеки aiogram.\n\n"
        "В проекте реализованы:\n"
        "- command-based архитектура\n"
        "- menu-driven архитектура\n"
        "- FSM архитектура"
    )

    await callback.answer()


# Main function
async def main():
    print("Бот запущен...")

    # Clear old updates
    await bot.delete_webhook(
        drop_pending_updates=True
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())