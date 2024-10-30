from sqlalchemy import select

from core import SubjectEnum, Subject, Score, Student
from core.base import get_session


async def get_missing_subjects(telegram_user_id: int) -> list[SubjectEnum]:
    """
    Получает список предметов, которые еще не добавлены пользователем.

    Args:
      telegram_user_id (int): Уникальный идентификатор пользователя в телеграмм.

    Returns:
      list[SubjectEnum]: Список отсутствующих предметов.
    """
    async with get_session() as session:
        # Получить список предметов, по которым у пользователя уже есть баллы
        existing_subjects = await session.execute(
            select(Subject.name).join(Score).join(Student).where(Student.telegram_user_id == telegram_user_id)
        )
        existing_subject_names = [subject.name for subject in existing_subjects.scalars()]

    missing_subjects = [
        subject for subject in SubjectEnum
        if subject.value not in existing_subject_names
    ]

    return missing_subjects
