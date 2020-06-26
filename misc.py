import logging
from aiogram import Bot, Dispatcher
from aiogram.bot import api
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqliter import SQLighter

import config

bot = Bot(token=config.token)
memory_storage = MemoryStorage()
db = SQLighter('users.db')
dp = Dispatcher(bot, storage=memory_storage)
PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
setattr(api, 'API_URL', PATCHED_URL)
logging.basicConfig(level=logging.INFO)