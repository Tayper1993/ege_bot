from sqlalchemy import String
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

    scores = relationship('Score', back_populates='student')
