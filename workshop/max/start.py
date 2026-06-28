from maxo import Bot, Router
from maxo.routing.filters import CommandStart, DeeplinkFilter
from maxo.routing.updates import BotStarted, MessageCreated
from maxo.types import User
from maxo.utils.builders import KeyboardBuilder

start_router = Router(__name__)


@start_router.bot_started(DeeplinkFilter())
async def bot_start_deeplink(bot_started: BotStarted, deeplink: str) -> None:
    await bot_started.send_message(text=f"Получил диплинк: {deeplink}", format=None)


@start_router.bot_started()
@start_router.message(CommandStart())  # Апасна, лучше отдельные хендлеры
async def bot_start(
    update: BotStarted | MessageCreated,  # Апасна, лучше отдельные хендлеры
    bot: Bot,
    event_from_user: User,
) -> None:
    workshop_url = "https://github.com/K1rL3s/mirea-max-bot-workshop"
    keyboard = (
        KeyboardBuilder()
        .add_link(text="🗄️Этот мастер-класс", url=workshop_url)
        .add_clipboard(text="🔁 Скопировать ссылку", payload=workshop_url)
        .add_message(text="✏️ Форматирование")
        .add_callback(text="📅 Календарь", payload="calendar")
        .add_request_contact(text="📞 Поделиться собой")
        .add_request_geo_location(text="📍 Выбрать локацию", quick=False)
        .add_request_geo_location(text="📍 Моя локация", quick=True)
        .add_open_app(text="🌐 Мини-апп", web_app=bot.state.info.username)
        .adjust(1, repeat=True)
        .build()
    )
    await update.send_message(
        text=f"Привет, {event_from_user.full_name}!",
        keyboard=keyboard,
        format=None,
    )
