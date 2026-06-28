from magic_filter import F
from maxo import Router
from maxo.integrations.magic_filter import MagicFilter
from maxo.routing.updates import CallbackQuery
from maxo.types import CallbackButton
from maxo.utils.builders import KeyboardBuilder

callback_router = Router(__name__)

EMPTY_SPACE = "⠀"


@callback_router.callback_query(MagicFilter(F.data == "calendar"))
async def callback_calendar(callback: CallbackQuery) -> None:
    await callback.answer(text="Я календарь, я календарь...")
    keyboard = (
        KeyboardBuilder()
        .add_callback("🗓️ Январь 1970", "empty")
        .add_callback("Пн", "empty")
        .add_callback("Вт", "empty")
        .add_callback("Ср", "empty")
        .add_callback("Чт", "empty")
        .add_callback("Пт", "empty")
        .add_callback("Сб", "empty")
        .add_callback("Вс", "empty")
        .add_callback(EMPTY_SPACE, "empty")
        .add_callback(EMPTY_SPACE, "empty")
        .add_callback(EMPTY_SPACE, "empty")
    )
    keyboard.add(
        *(CallbackButton(text=str(i), payload="empty") for i in range(1, 31 + 1)),
    )
    keyboard.add_callback(EMPTY_SPACE, "empty")
    keyboard.add_callback("⏪ Декабрь 1969", "empty")
    keyboard.add_callback("Февраль 1970 ⏩", "empty")
    keyboard.adjust(1, 7, 7, 7, 7, 7, 7, 2)
    await callback.edit_message(text="Календарь", keyboard=keyboard.build())


@callback_router.callback_query(MagicFilter(F.data == "empty"))
async def callback_empty(callback: CallbackQuery) -> None:
    await callback.answer(text="🤫🧏")
