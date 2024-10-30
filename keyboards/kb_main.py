from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Добавить предмет"),
      KeyboardButton(text="Посмотреть мои баллы")
    ],
    [
      KeyboardButton(text="Посмотреть мои предметы")
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=True
)