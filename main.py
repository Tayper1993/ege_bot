import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.settings import settings
from handlers.added_score import router_subject
from handlers.registration import router
from handlers.view_score import router_view_score


logging.basicConfig(level=logging.INFO)

API_TOKEN = settings.TOKEN
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


async def main():
    dp.include_router(router)
    dp.include_router(router_subject)
    dp.include_router(router_view_score)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
