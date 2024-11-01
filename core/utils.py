from functools import wraps

from aiogram import types
from sqlalchemy import select

from core import Student
from core.base import get_session


def check_user_registered(func):
    """
    Декоратор для проверки зарегистрирован ли пользователь в системе!
    :param func:
    :return:
    """

    @wraps(func)
    async def wrapper(message: types.Message, *args, **kwargs):
        async with get_session() as session:
            tg_user_id = message.from_user.id
            existing_student = await session.execute(select(Student).where(Student.telegram_user_id == tg_user_id))
            student = existing_student.scalars().first()

            if student is None:
                await message.reply('Вы не зарегистрированы!')
                return  # Прерываем выполнение функции, если пользователь не зарегистрирован

            return await func(
                message, *args, **kwargs
            )  # Вызываем оригинальную функцию, если пользователь зарегистрирован

    return wrapper
