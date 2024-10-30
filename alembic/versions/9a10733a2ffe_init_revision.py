"""init_revision

Revision ID: 9a10733a2ffe
Revises: 
Create Date: 2024-10-30 10:04:33.659666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a10733a2ffe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
    sa.Column('name', sa.String(length=200), nullable=False, comment='Имя'),
    sa.Column('surname', sa.String(length=200), nullable=False, comment='Фамилия'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
    sa.Column('name', sa.String(length=100), nullable=False, comment='Название школьного предмета'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('scores',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.SmallInteger(), nullable=False, comment='Баллы'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scores')
    op.drop_table('subjects')
    op.drop_table('students')
    # ### end Alembic commands ###