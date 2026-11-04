from dotenv import load_dotenv
load_dotenv()
from config import bot, dp
from logging_config import setup_logger
import logging
import asyncio

setup_logger()
dp.include_routers()
logger = logging.getLogger(__name__)

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

