import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


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


class Registration(StatesGroup):
    name = State()
    email = State()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\nВыберите действие:",
        reply_markup=menu
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — открыть главное меню\n"
        "/help — список команд\n"
        "/form — пример FSM-регистрации"
    )


@dp.message(Command("form"))
async def form_start(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer("Введите ваше имя:")


@dp.message(Registration.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.email)
    await message.answer("Введите адрес электронной почты:")


@dp.message(Registration.email)
async def process_email(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")

    await message.answer(
        f"Регистрация завершена.\n"
        f"Имя: {name}\n"
        f"Электронная почта: {message.text}"
    )

    await state.clear()


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
    await message.answer(
        "Данный Telegram-бот демонстрирует command-based, menu-driven и FSM-подходы."
    )


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())