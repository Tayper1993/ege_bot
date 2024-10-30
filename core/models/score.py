from sqlalchemy import SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base


class Score(Base):
    """
    Баллы ЕГЭ
    """

    __tablename__ = 'scores'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, comment='Идентификатор')

    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'), nullable=False)
    student = relationship('Student', back_populates='scores')

    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'), nullable=False)
    subject = relationship('Subject', back_populates='scores')

    score: Mapped[int] = mapped_column(SmallInteger, comment='Баллы', default=0)
