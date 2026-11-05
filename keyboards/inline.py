from aiogram.types import InlineKeyboardMarkup
from aiogram import types
from keyboards.callbacks import LangCB

lang_kb = InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text="Русский 🇷🇺", callback_data=LangCB(language="russian").pack()),
     types.InlineKeyboardButton(text="English 🇬🇧", callback_data=LangCB(language="english").pack())]
]
)