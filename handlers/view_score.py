from aiogram import F, Router, types
from aiogram.filters import Command

from commands.view_score import ViewScoreCommand
from core.base import get_session


router_view_score = Router()


@router_view_score.message(F.text == 'Посмотреть баллы')
@router_view_score.message(Command('view_scores'))
async def view_score_callback(message: types.Message):
    tg_user_id = int(message.from_user.id)

    async with get_session() as session:
        command = ViewScoreCommand(tg_user_id, session)
        result = await command.execute()
        await message.answer('Ваш результат:\n' + '\n'.join(result))
