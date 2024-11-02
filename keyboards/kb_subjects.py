from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core import Subject


async def get_subjects_keyboard(session: AsyncSession) -> ReplyKeyboardMarkup:
  subjects = await session.execute(select(Subject.name))
  subjects_result = subjects.all()
  keyboard = [
    [KeyboardButton(text=subject.name)] for subject in subjects_result
  ]
  return ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True,
    one_time_keyboard=True
  )