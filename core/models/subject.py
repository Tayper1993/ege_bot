from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base


class Subject(Base):
    """
    Школьные предметы
    """

    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, comment='Идентификатор')
    name: Mapped[str] = mapped_column(String(100), unique=True, comment='Название школьного предмета')

    scores = relationship('Score', back_populates='subject')
