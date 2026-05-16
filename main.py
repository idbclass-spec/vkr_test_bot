import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("Каталог", "Помощь")
menu.add("Контакты", "О боте")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать!\nВыберите действие:",
        reply_markup=menu
    )

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(
        "Доступные команды:\n/start\n/help"
    )

@dp.message_handler(lambda message: message.text == "Каталог")
async def catalog(message: types.Message):
    await message.answer("Раздел каталога: список товаров или услуг.")

@dp.message_handler(lambda message: message.text == "Помощь")
async def help_button(message: types.Message):
    await message.answer("Раздел помощи: выберите интересующий вопрос.")

@dp.message_handler(lambda message: message.text == "Контакты")
async def contacts(message: types.Message):
    await message.answer("Контакты: example@mail.ru")

@dp.message_handler(lambda message: message.text == "О боте")
async def about(message: types.Message):
    await message.answer("Данный Telegram-бот демонстрирует menu-driven интерфейс.")

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)