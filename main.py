import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


class Registration(StatesGroup):
    name = State()
    email = State()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\n"
        "Для регистрации введите команду /register.\n"
        "Для отмены используйте /cancel."
    )


@dp.message(Command("register"))
async def register_start(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer("Введите ваше имя:")


@dp.message(Registration.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.email)
    await message.answer("Введите адрес электронной почты:")


@dp.message(Registration.email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()

    await message.answer(
        "Регистрация завершена.\n"
        f"Имя: {data['name']}\n"
        f"Электронная почта: {data['email']}"
    )

    await state.clear()


@dp.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Регистрация отменена.")


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())