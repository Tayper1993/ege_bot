from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from commands.add_subject import AddSubjectCommand
from core.base import get_session

router_subject = Router()


class SubjectStates(StatesGroup):
    subject_name = State()


@router_subject.message(F.text == 'Добавить предмет')
async def add_subject(message: Message, state: FSMContext):
    await state.set_state(SubjectStates.subject_name)
    await message.reply("Введите название предмета:")


@router_subject.message(StateFilter(SubjectStates.subject_name))
async def process_subject_name(message: Message, state: FSMContext):
    subject_name = message.text
    tg_user_id = message.from_user.id

    async with get_session() as session:
        command = AddSubjectCommand(subject_name, session)  # Создайте команду для добавления предмета
        await command.execute()

    await message.answer(f"Предмет '{subject_name}' успешно добавлен!")
    await state.clear()  # Очистите состояние после добавления предмета
