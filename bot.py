from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import os
from dotenv import load_dotenv
from keybords import keyboard, keyboard_meal

load_dotenv()

bot_api = os.getenv('BOT_API')
bot = Bot(token=bot_api)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.full_name}!\nКакой вас интересует вопрос?',
                         reply_markup=keyboard)


@dp.message(F.text == 'Концепция все блюда за 400')
async def quastion(message: Message):
    await message.answer('Ебал я твой рот \n ddd \n aaa', reply_markup=keyboard_meal)


@dp.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.answer('Почта: test_mail@main.ru\nТелефон: 8 (800) 535 35-35')


@dp.message(F.text == 'Назад')
async def back(message: Message):
    await message.answer('Остались вопросы?', reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
