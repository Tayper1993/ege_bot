from core.models.student import Student
from sqlalchemy.ext.asyncio import AsyncSession


class RegisterStudentCommand:
    def __init__(
            self,
            name: str,
            surname: str,
            telegram_user_id: int,
            session: AsyncSession,
    ):
        self.name = name
        self.surname = surname
        self.session = session
        self.telegram_user_id = telegram_user_id

    async def execute(self):
        new_student = Student(name=self.name, surname=self.surname, telegram_user_id=self.telegram_user_id)
        async with self.session.begin():
            self.session.add(new_student)
