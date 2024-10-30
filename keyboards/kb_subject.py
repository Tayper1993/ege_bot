from aiogram import types

from core.utils import get_missing_subjects


async def create_subject_keyboard(telegram_user_id: int) -> types.ReplyKeyboardMarkup:
  """
  Создает клавиатуру с предметами, которые пользователь еще не добавил.
  """
  missing_subjects = await get_missing_subjects(telegram_user_id)

  keyboard_buttons = [
    types.KeyboardButton(text=subject.value) for subject in missing_subjects
  ]
  kb_subjects = types.ReplyKeyboardMarkup(
    keyboard=[
      keyboard_buttons[i:i + 2] for i in range(0, len(keyboard_buttons), 2)
    ],
    resize_keyboard=True
  )
  return kb_subjects