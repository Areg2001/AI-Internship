from aiogram.types import Message, Location, Dice
from commands.commands import set_commands
from keyboards.bottons import reply_keyboard
from keyboards.inlines import select_Iphone, select_emoji, get_inline_keyboard
from aiogram import Bot


async def get_start(message:Message, bot:Bot):
    await message.answer(f"Hi {message.from_user.first_name}", reply_markup=reply_keyboard)
    await set_commands(bot)


async def get_help(message:Message, bot:Bot):
    await message.answer("""
    Commands That can help you.
/start - Starting Bot.
/photo - Send you girl photo.
/video - Send you AI Video.
/mediagroup - Send you video+photo.
/document - Send you pdf file(auto questions).
/audio - Send you audio.
/help - Show you commands work with bot.
/iphone - Can see Iphone(It's test).
/by - By Iphone(test).
                        """)
    await set_commands(bot)


async def get_hello(message: Message, bot: Bot):
    await message.answer(f"Hello {message.from_user.first_name}. How are you")
    await set_commands(bot)


async def get_inline(message:Message, bot: Bot):
    await message.answer(f"{message.from_user.first_name} there are Iphone.", reply_markup=get_inline_keyboard())


async def show_emojis(message:Message, bot: Bot):
    await message.answer(f"{message.from_user.first_name} choose emoji.", reply_markup=select_emoji)
