from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot
from aiogram.utils.chat_action import ChatActionSender


async def send_audio(message: Message, bot: Bot):
    async with ChatActionSender.record_voice(chat_id=message.chat.id):
        audio = FSInputFile(path="/Users/aregmelqonyan/Desktop/Bot/2021-12-14_-_Space_Adventure_Intro_-_David_Fesliyan.mp3",
                            filename="AudiFile.mp3")
        await bot.send_audio(message.chat.id, audio=audio)


async def send_photo(message: Message, bot: Bot):
    async with ChatActionSender.upload_photo(chat_id=message.chat.id):
        photo = FSInputFile(path="/Users/aregmelqonyan/Desktop/Bot/photo.jpeg")
        await bot.send_photo(message.chat.id, photo, caption="Beautiful girl")


async def send_mediagroup(message: Message, bot: Bot):
    async with ChatActionSender.upload_video(chat_id=message.chat.id):
        photo = InputMediaPhoto(type="photo", media=FSInputFile(
            path="/Users/aregmelqonyan/Desktop/Bot/photo.jpeg"))
        video = InputMediaVideo(type="video",
                                media=FSInputFile(
                                    path="/Users/aregmelqonyan/Desktop/Bot/pexels-pavel-danilyuk-8327799-3840x2160-25fps.mp4"))
        media = [photo, video]
        await bot.send_media_group(message.chat.id, media)


async def send_video(message: Message, bot: Bot):
    async with ChatActionSender.upload_video(chat_id=message.chat.id):
        video = FSInputFile(path="/Users/aregmelqonyan/Desktop/Bot/pexels-pavel-danilyuk-8327799-3840x2160-25fps.mp4")
        await bot.send_video(message.chat.id, video)


async def send_document(message:Message, bot:Bot):
    async with ChatActionSender.upload_document(chat_id=message.chat.id):
        document = FSInputFile(path="/Users/aregmelqonyan/Desktop/Bot/1ff8bdd6ace0037a68d9dee4cc492bb1.pdf")
        await bot.send_document(message.chat.id, document)