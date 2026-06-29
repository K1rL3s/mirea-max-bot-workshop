from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.formatting import (
    BlockQuote,
    Bold,
    Italic,
    Strikethrough,
    Text,
    TextLink,
    TextMention,
    Underline,
)

message_router = Router(name=__name__)


@message_router.message(F.text == "✏️ Форматирование")
async def formatting_handler(message: Message) -> None:
    user = message.from_user

    text = Text(
        "Привет, это демонстрация возможностей форматирования текста.",
        "\n\n",
        Bold("Это жирный текст."),
        "\n",
        Italic("Это курсивный текст."),
        "\n",
        Underline("Это подчеркнутый текст."),
        "\n",
        Strikethrough("Это зачеркнутый текст."),
        "\n",
        TextLink("Это ссылка на библиотеку maxo.", url="https://github.com/K1rL3s/maxo"),
        "\n",
        "Это упоминание пользователя: ",
        TextMention(user=user),
        "\n",
        BlockQuote("Это цитата"),
    )

    await message.answer(text=text.as_html(), parse_mode=ParseMode.HTML)
    await message.answer(text=text.as_markdown(), parse_mode=ParseMode.MARKDOWN)


@message_router.message(F.text == "📍 Выбрать локацию")
async def choose_location_handler(message: Message) -> None:
    await message.answer("Это обычная кнопка. Нажми «📍 Моя локация» для отправки координат.")


@message_router.message(F.text)
async def text_handler(message: Message) -> None:
    await message.answer("Получил простое текстовое сообщение")
