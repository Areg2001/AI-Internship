from aiogram.types import CallbackQuery
from aiogram import Bot
from handlers.callbackdata import IphoneInfo
from keyboards.inlines import select_Iphone


async def select_iphone(call: CallbackQuery, bot: Bot, callback_data:IphoneInfo):
    model = callback_data.model
    make = callback_data.make
    year = callback_data.year
    answer = f"{call.message.chat.first_name} you select {model} {make} {year}. Be Happy!"

    await call.message.answer(text=answer)
    await call.answer()


async def select_emoji(call:CallbackQuery, bot:Bot):

    if call.data == "Casino-1":
        await call.message.answer_dice(emoji="🎰")
        await call.answer()
    elif call.data == "Football-1":
        await call.message.answer_dice(emoji="⚽")
        await call.answer()
    elif call.data == "Ball-1":
        await call.message.answer_dice(emoji="🎳")
        await call.answer()
    elif call.data == "Target-1":
        await call.message.answer_dice(emoji="🎯")
        await call.answer()
