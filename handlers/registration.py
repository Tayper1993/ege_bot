from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from sqlalchemy import select

from commands.register_student import RegisterStudentCommand
from core.base import get_session
from core.models.student import Student
from keyboards.kb_main import kb_main_menu
from keyboards.kb_registration import kb_yes_or_no


router = Router()


class RegistrationStates(StatesGroup):
    name = State()
    surname = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    async with get_session() as session:
        tg_user_id = message.from_user.id
        existing_student = await session.execute(select(Student).where(Student.telegram_user_id == tg_user_id))
        if existing_student.scalars().first():
            await message.reply('Вы уже зарегистрированы!', reply_markup=kb_main_menu)
            return

        await message.reply('Привет! Желаете зарегистрироваться?', reply_markup=kb_yes_or_no)


@router.message(F.text == 'Да')
@router.message(Command('register'))
async def process_name(message: Message, state: FSMContext):
    async with get_session() as session:
        tg_user_id = message.from_user.id
        existing_student = await session.execute(select(Student).where(Student.telegram_user_id == tg_user_id))
        if existing_student.scalars().first():
            await message.reply('Вы уже зарегистрированы!', reply_markup=kb_main_menu)
            return
    await state.set_state(RegistrationStates.name)
    await message.reply('Отлично! Введите ваше имя:')


@router.message(F.text == 'Нет')
async def close_bot(message: types.Message, state: FSMContext):
    await message.reply('Хорошо, если передумаете, просто напишите /start.')
    await state.clear()


@router.message(StateFilter(RegistrationStates.name))
async def process_surname(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.reply('Введите вашу фамилию:')
    await state.set_state(RegistrationStates.surname)


@router.message(StateFilter(RegistrationStates.surname))
async def register_user(message: Message, state: FSMContext):
    surname = message.text
    tg_user_id = message.from_user.id
    user_data = await state.get_data()
    name = user_data.get('name')

    async with get_session() as session:
        command = RegisterStudentCommand(name, surname, tg_user_id, session)
        await command.execute()

    await message.reply(f"Регистрация завершена! Добро пожаловать, {name} {surname}!", reply_markup=kb_main_menu)
    await state.clear()
