import os

from aiogram import Router
from aiogram.filters import CommandObject, CommandStart
from aiogram.types import CopyTextButton, Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

start_router = Router(name=__name__)
WORKSHOP_URL = "https://github.com/K1rL3s/mirea-max-bot-workshop"


def web_app_url() -> str | None:
    return os.environ.get("TG_WEB_APP_URL") or os.environ.get("WEB_APP_URL")


@start_router.message(CommandStart(deep_link=True))
async def bot_start_deeplink(message: Message, command: CommandObject) -> None:
    await message.answer(f"Получил диплинк: {command.args}")


@start_router.message(CommandStart())
async def bot_start(message: Message) -> None:
    user = message.from_user
    if user is None:
        return
    web_app = web_app_url()

    welcome_keyboard = InlineKeyboardBuilder()
    welcome_keyboard.button(text="🗄️ Этот мастер-класс", url=WORKSHOP_URL)
    welcome_keyboard.button(
        text="🔁 Скопировать ссылку",
        copy_text=CopyTextButton(text=WORKSHOP_URL),
    )
    welcome_keyboard.button(text="📅 Календарь", callback_data="calendar")
    welcome_keyboard.adjust(2, 1)

    reply_keyboard = ReplyKeyboardBuilder()
    reply_keyboard.button(text="✏️ Форматирование")
    reply_keyboard.button(text="📞 Поделиться собой", request_contact=True)
    reply_keyboard.button(text="📍 Выбрать локацию")
    reply_keyboard.button(text="📍 Моя локация", request_location=True)
    if web_app is not None:
        reply_keyboard.button(text="🌐 Мини-апп", web_app=WebAppInfo(url=web_app))
    reply_keyboard.adjust(1, 1, 2, 1)

    await message.answer(
        text=f"Привет, {user.full_name}!",
        reply_markup=welcome_keyboard.as_markup(),
    )
    await message.answer(
        text="Дополнительные кнопки для проверки reply-клавиатуры.",
        reply_markup=reply_keyboard.as_markup(resize_keyboard=True),
    )
