from aiogram import types, Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from commands.register_student import RegisterStudentCommand
from core.base import get_session
from keyboards.kb_registration import kb_yes_or_no

router_subject = Router()


class SubjectStates(StatesGroup):
    state_for_subject = State()


# @router_subject.message()