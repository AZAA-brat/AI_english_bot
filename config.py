from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
load_dotenv()
import os

bot_token = os.getenv("BOT_TOKEN")
bot = Bot(token=bot_token)
dp = Dispatcher()
