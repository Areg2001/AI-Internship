from aiogram.filters.callback_data import CallbackData


class IphoneInfo(CallbackData, prefix="Iphone"):
    model: str
    make: str
    year: int
