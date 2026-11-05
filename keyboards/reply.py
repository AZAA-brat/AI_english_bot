from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.phrases import get_phrase

def choice(lang):
    choice_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_phrase("translate", lang)),
            KeyboardButton(text=get_phrase("grammar", lang))],
            [KeyboardButton(text=get_phrase("writing", lang)),
             KeyboardButton(text=get_phrase("lang_change", lang))],
        ]
    )
    return choice_kb