from core.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession


class RegisterUserCommand:
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
        new_user = User(name=self.name, surname=self.surname)
        async with self.session.begin():
            self.session.add(new_user)
