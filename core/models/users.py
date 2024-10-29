from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from core.base import Base


class User(Base):
    """
    Пользователи
    """

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, comment='Идентификатор')
    name: Mapped[str] = mapped_column(String(1000), comment='Имя')
    surname: Mapped[str] = mapped_column(String(200), comment='Фамилия')