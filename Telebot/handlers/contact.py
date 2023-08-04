from aiogram.types import Message
from aiogram import Bot

async def get_true_contact(message: Message, bot: Bot, phone):
    await message.answer(f"{message.from_user.first_name} you are sended true contact {phone}.")

async def get_false_contact(message: Message, bot: Bot, phone):
    await message.answer(f"{message.from_user.first_name} you are sended false contact {phone}.")
