from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from mako.testing.helpers import result_lines

from sqlalchemy import select

from commands.add_score import AddScoreCommand
from core import Student, Subject, Score
from core.base import get_session
from core.models import student, subject
from keyboards.kb_main import kb_main_menu
from keyboards.kb_subject import create_subject_keyboard

router_subject = Router()


class ScoreStates(StatesGroup):
    subject_name = State()
    score = State()


@router_subject.message(F.text == 'Добавить баллы')
async def cmd_add_score(message: types.Message, state: FSMContext):
    await state.set_state(ScoreStates.subject_name)
    await message.reply('Отлично! Введите предмет по которому вы хотите внести баллы')


@router_subject.message(StateFilter(ScoreStates.subject_name))
async def cmd_add_score(message: types.Message, state: FSMContext):
    subject_name = message.text
    await state.update_data(subject_name=subject_name)
    await message.reply('Введите количество баллов')
    await state.set_state(ScoreStates.score)


@router_subject.message(StateFilter(ScoreStates.score))
async def cmd_add_score(message: types.Message, state: FSMContext):
    score = int(message.text)
    tg_user_id = message.from_user.id
    user_data = await state.get_data()
    subject_name = user_data.get('subject_name')

    async with get_session() as session:
        student_query = await session.execute(select(Student).where(Student.telegram_user_id == tg_user_id))
        result_student_query = student_query.scalars().first()

        subject_query = await session.execute(select(Subject).where(Subject.name == subject_name))
        result_subject_query = subject_query.scalars().first()

        score_query = await session.execute(
            select(
                Score
            ).where(
                Score.student_id == result_student_query.id,
                Score.subject_id == result_subject_query.id,
            )
        )
        result_score_query = score_query.scalars().first()

        if result_score_query:
            result_score_query.score = score
            await session.merge(result_score_query)  # Обновление записи в сессии
            await session.commit()
        else:
            command = AddScoreCommand(
                student_id=result_student_query.id,
                subject_id=result_subject_query.id,
                score=score,
                session=session,
            )
            await command.execute()

    await message.reply(f"Количество баллов занесено", reply_markup=kb_main_menu)
    await state.clear()
