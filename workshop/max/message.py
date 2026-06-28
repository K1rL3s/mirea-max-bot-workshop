from magic_filter import F
from maxo import Router
from maxo.enums import TextFormat
from maxo.integrations.magic_filter import MagicFilter
from maxo.routing.updates import MessageCreated
from maxo.utils.formatting import (
    BlockQuote,
    Bold,
    Heading,
    Highlighted,
    Italic,
    Link,
    Mention,
    Monospaced,
    Strikethrough,
    Text,
    Underline,
)

message_router = Router(__name__)


@message_router.message(MagicFilter(F.message.body.text == "✏️ Форматирование"))
async def formatting_handler(message: MessageCreated) -> None:
    text = Text(
        Heading("Привет, это демонстрация возможностей форматирования текста."),
        "\n\n",
        Bold("Это жирный текст."),
        "\n",
        Italic("Это курсивный текст."),
        "\n",
        Underline("Это подчеркнутый текст."),
        "\n",
        Strikethrough("Это зачеркнутый текст."),
        "\n",
        Monospaced("Это моноширинный текст."),
        "\n",
        Link("Это ссылка на библиотеку maxo.", url="https://github.com/K1rL3s/maxo"),
        "\n",
        "Это упоминание пользователя: ",
        Mention(
            message.message.unsafe_sender.fullname,
            user_id=message.message.unsafe_sender.id,
        ),
        "\n",
        Highlighted("Это выделенный текст"),
        "\n",
        BlockQuote("Это цитата"),
    )

    await message.answer(text=text.as_html(), format=TextFormat.HTML)
    await message.answer(text=text.as_markdown(), format=TextFormat.MARKDOWN)
