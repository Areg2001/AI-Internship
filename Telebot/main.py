import contextlib
from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import Command
from handlers.basic import get_start, get_inline, get_help, get_hello, show_emojis
from handlers.pay import order
from handlers.pay import successful_payment, pre_checkout_query
from handlers.callback import select_iphone, select_emoji
from handlers.send_media import send_photo, send_audio, send_mediagroup, send_video, send_document
from aiogram import F
from handlers.callbackdata import IphoneInfo

token = "6213787899:AAGfZE2Y2pD-N2FR7t1Cjqm0Vsq5Qszccyw"


async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.message.register(get_start, Command(commands="start"))
    dp.message.register(get_inline, Command(commands='iphone'))
    dp.message.register(get_help, Command(commands='help'))
    dp.message.register(order, Command(commands='by'))
    dp.message.register(get_hello, Command(commands="hello"))
    dp.message.register(send_audio, Command(commands="audio"))
    dp.message.register(send_photo, Command(commands="photo"))
    dp.message.register(send_video, Command(commands="video"))
    dp.message.register(send_mediagroup, Command(commands="mediagroup"))
    dp.message.register(send_document, Command(commands="document"))
    dp.message.register(show_emojis, Command(commands="emojis"))
    dp.callback_query.register(select_iphone, IphoneInfo.filter(F.model == "iphone"))
    dp.callback_query.register(select_emoji)

    dp.pre_checkout_query.register(pre_checkout_query)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())