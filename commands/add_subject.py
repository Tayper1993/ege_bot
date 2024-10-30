from core.models.subject import Subject
from sqlalchemy.ext.asyncio import AsyncSession


class AddSubjectCommand:
    def __init__(self, name: str, session: AsyncSession):
        self.name = name
        self.session = session

    async def execute(self):
        add_subject = Subject(name=self.name)

        async with self.session.begin():
            self.session.add(add_subject)
