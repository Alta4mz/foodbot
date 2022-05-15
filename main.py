import logging
from aiogram import executor
from createbot import dp
import handler
from handlers import menu

logging.basicConfig(level=logging.INFO)

handler.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)