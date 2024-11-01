from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core import Score, Student, Subject


class ViewScoreCommand:
    def __init__(self, telegram_user_id: int, session: AsyncSession):
        self.telegram_user_id = telegram_user_id
        self.session = session

    async def execute(self):
        student_query = (
            select(Student.name, Score.score, Subject.name)
            .join(Score, Score.student_id == Student.id, isouter=True)
            .join(Subject, Subject.id == Score.subject_id, isouter=True)
            .where(Student.telegram_user_id == self.telegram_user_id)
        )

        results = await self.session.execute(student_query)
        students = results.all()

        return [
            f"Студент: {student_name}, Предмет: {subject_name}, Оценка: {score}, "
            for student_name, score, subject_name in students
        ]
