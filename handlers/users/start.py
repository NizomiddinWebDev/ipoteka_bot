from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat_filter import IsPrivate
from loader import dp
from utils.misc.allmethods import check_user


@dp.message_handler(IsPrivate(), CommandStart())
async def start(message: types.Message):
    await check_user(message.chat.id, message.from_user.id, message.from_user.full_name)
