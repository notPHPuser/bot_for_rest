from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_meal = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Когда все блюда за 400')], [KeyboardButton(text='Назад')]],
                                    resize_keyboard=True)

keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Концепция все блюда за 400")], [KeyboardButton(text='Контакты')]],
    resize_keyboard=True)
