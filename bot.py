from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart, Command
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

bot_api = os.getenv('BOT_API')
bot = Bot(token=bot_api)
dp = Dispatcher()


keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Концепция все блюда за 400")], [KeyboardButton(text='Контакты')]],
    resize_keyboard=True)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Какой вас интересует вопрос?', reply_markup=keyboard)


# @dp.message(F.text == 'Концепция все блюда за 400')
# async def quastion(message: Message):
#     await message.answer('Ебал я твой рот \n ddd \n aaa')

@dp.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.answer('Почта: test_mail@main.ru\nТелефон: 8 (800) 535 35-35')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
