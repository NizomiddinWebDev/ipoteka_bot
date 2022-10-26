from aiogram import types
from aiogram.dispatcher.filters import filters
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from states.userState import UserState
from utils.db_api.model import getUser
from utils.misc.allmethods import send_error, send_call_bank_message, send_main_menu, send_error_choice
from data import const_data as const


@dp.message_handler(state=UserState.contact_us)
async def contact_us_handler(message: types.Message):
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    if not user:
        await send_error(message.chat)
    elif message.text == const.CALL_BANK[user.lang]:
        await send_call_bank_message(message.chat.id, user.lang)
    elif message.text == const.WRITE_CONSULTANT[user.lang]:
        pass
    elif message.text == const.BACK[user.lang]:
        await send_main_menu(user)
    else:
        await send_error_choice(message.chat.id, user.lang)
