import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from workshop.runner import run
from workshop.tg.attachments import attachments_router
from workshop.tg.callback import callback_router
from workshop.tg.message import message_router
from workshop.tg.start import start_router

logger = logging.getLogger(__name__)


async def set_bot_commands(bot: Bot) -> None:
    await bot.set_my_name(name="Maxo Бот")
    await bot.set_my_description(
        description=(
            "Демонстрационный бот Python фреймворка aiogram\n"
            "https://github.com/aiogram/aiogram"
        ),
    )
    result = await bot.set_my_commands(
        [BotCommand(command="start", description="Старт")],
    )
    logger.info("%s", result)


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        start_router,
        callback_router,
        message_router,
        attachments_router,
    )

    bot = Bot(token=os.environ["TG_TOKEN"])
    await set_bot_commands(bot)
    await dp.start_polling(bot, drop_pending_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    run(main())
