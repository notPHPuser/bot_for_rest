from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart, Command
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

bot_api = os.getenv('BOT_API')
bot = Bot(token=bot_api)
dp = Dispatcher()
keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Концепция все блюда за 400")], [KeyboardButton(text='Контакты')]], resize_keyboard=True)
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Какой вас интересует вопрос?', reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')