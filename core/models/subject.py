from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base
from core.models.enums import SubjectEnum


class Subject(Base):
    """
    Школьные предметы
    """

    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, comment='Идентификатор')
    name: Mapped[str] = mapped_column(String, comment='Название школьного предмета')

    scores = relationship('Score', back_populates='subject')
