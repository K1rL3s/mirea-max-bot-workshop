from aiogram import F, Router
from aiogram.types import Message

attachments_router = Router(name=__name__)


@attachments_router.message(F.audio)
async def audio_handler(message: Message) -> None:
    await message.answer("Получил аудиофайл")
    await message.copy_to(chat_id=message.chat.id)


@attachments_router.message(F.document)
async def document_handler(message: Message) -> None:
    await message.answer("Получил сообщение с файлом")
    await message.copy_to(chat_id=message.chat.id)


@attachments_router.message(F.photo)
async def image_handler(message: Message) -> None:
    await message.answer("Получил сообщение с изображениями")
    await message.copy_to(chat_id=message.chat.id)


@attachments_router.message(F.sticker)
async def sticker_handler(message: Message) -> None:
    await message.answer("Получил сообщение со стикером")
    await message.copy_to(chat_id=message.chat.id)


@attachments_router.message(F.video)
async def video_handler(message: Message) -> None:
    await message.answer("Получил сообщение с видео")
    await message.copy_to(chat_id=message.chat.id)


@attachments_router.message(F.voice)
async def voice_handler(message: Message) -> None:
    await message.answer("Получил голосовое сообщение")
    await message.copy_to(chat_id=message.chat.id)


@attachments_router.message(F.contact)
async def attachment_contact_handler(message: Message) -> None:
    await message.answer("Получил сообщение с контактом")
    await message.copy_to(chat_id=message.chat.id)


@attachments_router.message(F.location)
async def attachment_location_handler(message: Message) -> None:
    await message.answer("Получил сообщение с геопозицией")
    await message.copy_to(chat_id=message.chat.id)
