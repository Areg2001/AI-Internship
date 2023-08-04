from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.callbackdata import IphoneInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


select_Iphone = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Iphone 14 Pro 2022",
                             callback_data="iphone_14Pro_2022",
                             url="http://icentre.am/Default.aspx?CategoryID=-1&Page=0&ProductID=173042&SearchText=Iphone+14+Pro")
    ],

    [
        InlineKeyboardButton(text="Iphone 6S 2012",
                             callback_data="iphone_6S_2012"
                             )
    ],

    [
        InlineKeyboardButton(text="Iphone 13 2017",
                             callback_data="iphone_13_2017",
                             url="http://icentre.am/Default.aspx?CategoryID=-1&Page=0&ProductID=172762&SearchText=Iphone+13")
    ]
])

select_emoji = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Casino",
                             callback_data="Casino-1")
    ],

    [
        InlineKeyboardButton(text="Football",
                             callback_data="Football-1")
    ],

    [
        InlineKeyboardButton(
            text="Ball",
            callback_data="Ball-1")
    ],

    [
        InlineKeyboardButton(
            text="Target",
            callback_data="Target-1"
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Iphone 14 Pro 2022",
                            callback_data=IphoneInfo(model='iphone', make='14Pro', year=2022),
                            url="http://icentre.am/Default.aspx?CategoryID=-1&Page=0&ProductID=173042&SearchText=Iphone+14+Pro")
    keyboard_builder.button(text="Iphone 6S 2012",
                            callback_data=IphoneInfo(model='iphone', make='6S', year=2012))
    keyboard_builder.button(text="Iphone 13 2017",
                            callback_data=IphoneInfo(model='iphone', make='13', year=2017),
                            url="http://icentre.am/Default.aspx?CategoryID=-1&Page=0&ProductID=172762&SearchText=Iphone+13")
    keyboard_builder.adjust(3)

    return keyboard_builder.as_markup()

