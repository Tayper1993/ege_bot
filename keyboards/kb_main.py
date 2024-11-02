from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить баллы'), KeyboardButton(text='Посмотреть баллы')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
