from core import SubjectEnum
from core.models.subject import Subject
from sqlalchemy.ext.asyncio import AsyncSession


class AddSubjectCommand:
    def __init__(self, subject_enum: SubjectEnum, session: AsyncSession):
        self.subject_enum = subject_enum
        self.session = session

    async def execute(self):
        add_subject = Subject(name=self.subject_enum)

        async with self.session.begin():
            self.session.add(add_subject)
