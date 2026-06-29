from maxo import Ctx, Router
from maxo.enums import AttachmentType
from maxo.routing.filters import BaseFilter
from maxo.routing.updates import MessageCreated

attachments_router = Router(__name__)


class AttachmentFilter(BaseFilter[MessageCreated]):
    def __init__(self, attachment_type: AttachmentType) -> None:
        self._attachment_type = attachment_type

    async def __call__(self, message: MessageCreated, ctx: Ctx) -> bool:
        for attachment in message.message.body.attachments or []:
            if attachment.type == self._attachment_type:
                return True

        # ruff: noqa: SIM103
        if self._attachment_type == AttachmentType.TEXT and message.message.body.text:
            return True

        return False


@attachments_router.message_created(AttachmentFilter(AttachmentType.AUDIO))
async def audio_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил голосовое сообщение")
    await message.send_message(
        media=[message.message.body.audio.to_request()],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.CONTACT))
async def contact_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил сообщение с контактом")
    await message.bot.send_message(
        chat_id=message.chat_id,
        attachments=[message.message.body.contact],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.FILE))
async def file_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил сообщение с файлом")
    await message.send_message(
        media=[message.message.body.file.to_request()],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.IMAGE))
async def image_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил сообщение с изображениями")
    await message.send_message(
        media=[photo.to_request() for photo in message.message.body.photo],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.LOCATION))
async def location_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил сообщение с геопозицией")
    await message.bot.send_message(
        chat_id=message.chat_id,
        attachments=[message.message.body.location],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.SHARE))
async def share_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил сообщение с предпросмотром ссылки")
    await message.bot.send_message(
        chat_id=message.chat_id,
        attachments=[message.message.body.share],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.STICKER))
async def sticker_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил сообщение со стикером")
    await message.bot.send_message(
        chat_id=message.chat_id,
        attachments=[message.message.body.sticker],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.VIDEO))
async def video_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил сообщение с видео")
    await message.send_message(
        media=[video.to_request() for video in message.message.body.video],
    )


@attachments_router.message_created(AttachmentFilter(AttachmentType.TEXT))
async def text_handler(message: MessageCreated) -> None:
    await message.answer_text("Получил простое текстовое сообщение")
