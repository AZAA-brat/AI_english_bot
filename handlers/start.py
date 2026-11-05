from aiogram import Router, types
from aiogram.filters import CommandStart
from utils.phrases import get_phrase
from states import Registration
from keyboards.inline import lang_kb
from keyboards.reply import choice
from storage.db import add_user, get_user

router = Router()
@router.message(CommandStart())
async def start(message: types.Message):
    await add_user(
        message.from_user.id,
        message.from_user.first_name
    )
    user = await get_user(
        message.from_user.id
    )
    await message.answer(get_phrase())
