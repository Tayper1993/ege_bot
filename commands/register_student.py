from core.models.student import Student
from sqlalchemy.ext.asyncio import AsyncSession


class RegisterStudentCommand:
    def __init__(
            self,
            name: str,
            surname: str,
            session: AsyncSession,
    ):
        self.name = name
        self.surname = surname
        self.session = session

    async def execute(self):
        new_student = Student(name=self.name, surname=self.surname)
        async with self.session.begin():
            self.session.add(new_student)
