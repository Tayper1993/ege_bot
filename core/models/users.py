from sqlalchemy import String, SmallInteger, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from core.base import Base


class User(Base):
    """
    Пользователи
    """

    __tablename__ = 'user'

    __table_args__ = (
        CheckConstraint('score >= 0 AND score <= 100', name='check_score_range'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, comment='Идентификатор')
    name: Mapped[str] = mapped_column(String(1000), comment='Имя')
    surname: Mapped[str] = mapped_column(String(200), comment='Фамилия')
    score: Mapped[int] = mapped_column(SmallInteger, comment='Баллы', default=0)
