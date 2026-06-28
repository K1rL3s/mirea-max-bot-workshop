import os

from maxo import Bot, Dispatcher
from maxo.fsm.key_builder import DefaultKeyBuilder
from maxo.fsm.storages.memory import MemoryStorage
from maxo.transport.long_polling import LongPolling

from workshop.runner import run


async def main() -> None:
    key_builder = DefaultKeyBuilder(with_destiny=True)
    storage = MemoryStorage(key_builder=key_builder)
    dp = Dispatcher(storage=storage)

    bot = Bot(token=os.environ["MAX_TOKEN"])

    await LongPolling(dispatcher=dp).start(bot=bot, drop_pending_updates=True)


if __name__ == "__main__":
    run(main())
