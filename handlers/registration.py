from aiogram import types, Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from commands.register_user import RegisterUserCommand
from core.base import get_session
from keyboards.kb_registration import kb_yes_or_no

router = Router()


class RegistrationStates(StatesGroup):
    state_for_name = State()
    state_for_surname = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Привет! Желаете зарегистрироваться?", reply_markup=kb_yes_or_no)


@router.message(F.text == 'Да')
async def process_name(message: Message, state: FSMContext):
    await state.set_state(RegistrationStates.state_for_name)
    await message.reply('Отлично! Введите ваше имя:')


@router.message(F.text == 'Нет')
async def close_bot(message: types.Message, state: FSMContext):
    await message.reply("До свидания!")
    await state.clear()


@router.message(StateFilter(RegistrationStates.state_for_name))
async def process_surname(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.reply('Введите вашу фамилию:')
    await state.set_state(RegistrationStates.state_for_surname)


@router.message(StateFilter(RegistrationStates.state_for_surname))
async def register_user(message: Message, state: FSMContext):
    surname = message.text
    user_data = await state.get_data()
    name = user_data.get('name')

    async with get_session() as session:
        command = RegisterUserCommand(name, surname, session)
        await command.execute()

    await message.answer(f"Регистрация завершена! Добро пожаловать, {name} {surname}!")
    await state.clear()
