from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from sqlalchemy import select

from commands.add_subject import AddSubjectCommand
from core import SubjectEnum, Subject
from core.base import get_session
from keyboards.kb_main import kb_main_menu
from keyboards.kb_subject import create_subject_keyboard

router_subject = Router()


class SubjectStates(StatesGroup):
    subject_name = State()


@router_subject.message(F.text == 'Добавить предмет')
async def cmd_add_subject(message: types.Message, state: FSMContext):
    telegram_user_id = message.from_user.id
    kb_subjects = await create_subject_keyboard(telegram_user_id)  # Получите клавиатуру

    if kb_subjects.keyboard:
        await message.answer("Выберите предмет:", reply_markup=kb_subjects)
        await state.set_state(SubjectStates.subject_name)
    else:
        await message.answer("Вы уже добавили все предметы.")


@router_subject.message(StateFilter(SubjectStates.subject_name))
async def add_subject(message: types.Message, state: FSMContext):
    subject_name = message.text

    subject_enum = next((subject for subject in SubjectEnum if subject.value == subject_name), None)

    if subject_enum is None:
        await message.reply("Пожалуйста, выберите предмет из списка.")
        return

    async with get_session() as session:
        command = AddSubjectCommand(subject_enum, session)
        await command.execute()

    await message.reply(f"Предмет '{subject_name}' успешно добавлен!", reply_markup=kb_main_menu)
    await state.clear()  # Очистите состояние после добавления предмета
