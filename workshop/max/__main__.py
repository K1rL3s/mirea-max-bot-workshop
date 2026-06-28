import logging
import os

from maxo import Bot, Dispatcher
from maxo.fsm.key_builder import DefaultKeyBuilder
from maxo.fsm.storages.memory import MemoryStorage
from maxo.transport.long_polling import LongPolling
from maxo.types import BotCommand

from workshop.max.callback import callback_router
from workshop.max.start import start_router
from workshop.max.message import message_router
from workshop.runner import run

logger = logging.getLogger(__name__)


async def set_bot_commands(bot: Bot) -> None:
    result = await bot.edit_bot_info(
        first_name="Maxo Бот",
        last_name=None,
        description=(
            "Демонстрационный бот Python фреймворка Maxo\n"
            "https://github.com/K1rL3s/maxo\n"
            "https://pypi.org/project/maxo"
        ),
        commands=[BotCommand(name="start", description="Старт")],
    )
    logger.info("%s", result)


async def main() -> None:
    key_builder = DefaultKeyBuilder(with_destiny=True)
    storage = MemoryStorage(key_builder=key_builder)
    dp = Dispatcher(storage=storage)

    dp.include(
        start_router,
        callback_router,
        message_router,
    )
    # dp.after_startup.register(set_bot_commands)

    bot = Bot(token=os.environ["MAX_TOKEN"])

    await LongPolling(dispatcher=dp).start(bot=bot, drop_pending_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    run(main())
