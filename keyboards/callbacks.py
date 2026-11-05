from aiogram.filters.callback_data import CallbackData

class LangCB(CallbackData, prefix="language"):
    language: str

