from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

callback_router = Router(name=__name__)


@callback_router.callback_query(F.data == "calendar")
async def callback_calendar(callback: CallbackQuery) -> None:
    await callback.answer("Я календарь, я календарь...")\

    calendar_keyboard = InlineKeyboardBuilder()
    calendar_keyboard.row(
        InlineKeyboardButton(text="🗓️ Январь 1970", callback_data="empty")
    )
    calendar_keyboard.row(
        InlineKeyboardButton(text="Пн", callback_data="empty"),
        InlineKeyboardButton(text="Вт", callback_data="empty"),
        InlineKeyboardButton(text="Ср", callback_data="empty"),
        InlineKeyboardButton(text="Чт", callback_data="empty"),
        InlineKeyboardButton(text="Пт", callback_data="empty"),
        InlineKeyboardButton(text="Сб", callback_data="empty"),
        InlineKeyboardButton(text="Вс", callback_data="empty"),
    )
    calendar_keyboard.row(
        InlineKeyboardButton(text=" ", callback_data="empty"),
        InlineKeyboardButton(text=" ", callback_data="empty"),
        InlineKeyboardButton(text=" ", callback_data="empty"),
        InlineKeyboardButton(text="1", callback_data="empty"),
        InlineKeyboardButton(text="2", callback_data="empty"),
        InlineKeyboardButton(text="3", callback_data="empty"),
        InlineKeyboardButton(text="4", callback_data="empty"),
    )
    calendar_keyboard.row(
        InlineKeyboardButton(text="5", callback_data="empty"),
        InlineKeyboardButton(text="6", callback_data="empty"),
        InlineKeyboardButton(text="7", callback_data="empty"),
        InlineKeyboardButton(text="8", callback_data="empty"),
        InlineKeyboardButton(text="9", callback_data="empty"),
        InlineKeyboardButton(text="10", callback_data="empty"),
        InlineKeyboardButton(text="11", callback_data="empty"),
    )
    calendar_keyboard.row(
        InlineKeyboardButton(text="12", callback_data="empty"),
        InlineKeyboardButton(text="13", callback_data="empty"),
        InlineKeyboardButton(text="14", callback_data="empty"),
        InlineKeyboardButton(text="15", callback_data="empty"),
        InlineKeyboardButton(text="16", callback_data="empty"),
        InlineKeyboardButton(text="17", callback_data="empty"),
        InlineKeyboardButton(text="18", callback_data="empty"),
    )
    calendar_keyboard.row(
        InlineKeyboardButton(text="19", callback_data="empty"),
        InlineKeyboardButton(text="20", callback_data="empty"),
        InlineKeyboardButton(text="21", callback_data="empty"),
        InlineKeyboardButton(text="22", callback_data="empty"),
        InlineKeyboardButton(text="23", callback_data="empty"),
        InlineKeyboardButton(text="24", callback_data="empty"),
        InlineKeyboardButton(text="25", callback_data="empty"),
    )
    calendar_keyboard.row(
        InlineKeyboardButton(text="26", callback_data="empty"),
        InlineKeyboardButton(text="27", callback_data="empty"),
        InlineKeyboardButton(text="28", callback_data="empty"),
        InlineKeyboardButton(text="29", callback_data="empty"),
        InlineKeyboardButton(text="30", callback_data="empty"),
        InlineKeyboardButton(text="31", callback_data="empty"),
        InlineKeyboardButton(text=" ", callback_data="empty"),
    )
    calendar_keyboard.row(
        InlineKeyboardButton(text="⏪ Декабрь 1969", callback_data="empty"),
        InlineKeyboardButton(text="Февраль 1970 ⏩", callback_data="empty"),
    )

    await callback.message.edit_text(
        text="Календарь",
        reply_markup=calendar_keyboard.as_markup(),
    )


@callback_router.callback_query(F.data == "empty")
async def callback_empty(callback: CallbackQuery) -> None:
    await callback.answer("🤫🧏")
