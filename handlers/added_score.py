from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy import select

from commands.add_score import AddScoreCommand
from core import Score, Student, Subject
from core.base import get_session
from core.utils import check_user_registered
from keyboards.kb_main import kb_main_menu
from keyboards.kb_subjects import get_subjects_keyboard

router_subject = Router()


class ScoreStates(StatesGroup):
    subject_name = State()
    score = State()


@router_subject.message(F.text == 'Добавить баллы')
@router_subject.message(Command('enter_scores'))
@check_user_registered
async def start_score_addition(message: types.Message, state: FSMContext):
    await state.set_state(ScoreStates.subject_name)
    async with get_session() as session:
        kb_subjects = await get_subjects_keyboard(session)
    await message.reply('Отлично! Введите предмет по которому вы хотите внести баллы', reply_markup=kb_subjects)


@router_subject.message(StateFilter(ScoreStates.subject_name))
async def set_subject_name(message: types.Message, state: FSMContext):
    subject_name = message.text
    await state.update_data(subject_name=subject_name)
    await message.reply('Введите количество баллов')
    await state.set_state(ScoreStates.score)


@router_subject.message(StateFilter(ScoreStates.score))
async def set_score_value(message: types.Message, state: FSMContext):
    score = int(message.text)
    tg_user_id = message.from_user.id
    user_data = await state.get_data()
    subject_name = user_data.get('subject_name')

    async with get_session() as session:
        student_query = await session.execute(select(Student).where(Student.telegram_user_id == tg_user_id))
        result_student_query = student_query.scalars().first()

        if result_student_query is None:
            await message.answer('Такого студента нету')
            await state.clear()

        subject_query = await session.execute(select(Subject).where(Subject.name == subject_name))
        result_subject_query = subject_query.scalars().first()

        if result_subject_query is None:
            await message.answer('Вы не добавили предмет')
            await state.clear()

        score_query = await session.execute(
            select(Score).where(
                Score.student_id == result_student_query.id,
                Score.subject_id == result_subject_query.id,
            )
        )
        result_score_query = score_query.scalars().first()

        if result_score_query:
            result_score_query.score = score
            await session.merge(result_score_query)
            await session.commit()
        else:
            command = AddScoreCommand(
                student_id=result_student_query.id,
                subject_id=result_subject_query.id,
                score=score,
                session=session,
            )
            await command.execute()

    await message.reply('Количество баллов занесено', reply_markup=kb_main_menu)
    await state.clear()
