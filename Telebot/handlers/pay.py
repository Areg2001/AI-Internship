from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Boti mijocov iphonner areq",
        description="Caxum em Iphonner matcheli gnerov",
        payload="Cherez telegram tal poxn brat",
        provider_token='381764678:TEST:59580',
        currency='rub',
        prices =[
            LabeledPrice(
                label="Price",
                amount="30000"
            ),
            LabeledPrice(
                label="NDS",
                amount="22000"
            ),
            LabeledPrice(
                label="bonusova",
                amount=-2000
            )
        ],
        max_tip_amount=6000,
        suggested_tip_amounts=[2000, 3000, 4000, 5000],
        start_parameter="Coder",
        provider_data=None,
        photo_url='https://1000logos.net/wp-content/uploads/2020/05/Google-Photos-logo.png',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=20
    )

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successful_payment(message: Message):
    await message.answer("Payment verified we will call you, Thanks")