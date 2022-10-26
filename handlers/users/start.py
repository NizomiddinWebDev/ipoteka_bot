from aiogram import types
from aiogram.dispatcher.filters import filters

from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from utils.db_api.model import new_user_add, getUser

from utils.misc.allmethods import check_user


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await check_user(message.chat.id,message.from_user.id)
