from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base


class Student(Base):
    """
    Пользователи
    """

    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, comment='Идентификатор')
    name: Mapped[str] = mapped_column(String(200), comment='Имя')
    surname: Mapped[str] = mapped_column(String(200), comment='Фамилия')
    telegram_user_id: Mapped[int] = mapped_column(
        Integer, unique=True, comment='Уникальный идентификатор пользователя в телеграмм'
    )

    scores = relationship('Score', back_populates='student')
