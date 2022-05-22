from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_Token = 'Не для посторонних глаз'


storage = MemoryStorage()

bot = Bot(token=API_Token)
dp = Dispatcher(bot, storage=storage)