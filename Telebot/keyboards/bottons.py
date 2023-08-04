from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="/start"),
        KeyboardButton(text="/iphone"),
        KeyboardButton(text="/by")
    ],
    [
        KeyboardButton(text="/photo"),
        KeyboardButton(text="/video"),
        KeyboardButton(text="/document")
    ],
    [
        KeyboardButton(text="/audio"),
        KeyboardButton(text="/mediagroup"),
        KeyboardButton(text="/help"),
        KeyboardButton(text="Victorina", request_poll=KeyboardButtonPollType())
    ]
], one_time_keyboard=False)
