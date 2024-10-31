from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить предмет'), KeyboardButton(text='Добавить баллы')],
        [KeyboardButton(text='Посмотреть мои предметы')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
