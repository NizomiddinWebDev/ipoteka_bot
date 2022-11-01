from aiogram import types
from filters.private_chat_filter import IsPrivate
from loader import dp, bot
from states.userState import UserState
from utils.db_api.model import getUser
from data import const_data as const
from utils.misc.allmethods import send_error, send_change_language, send_main_menu


@dp.message_handler(IsPrivate(), state=UserState.settings)
@dp.message_handler(IsPrivate())
async def settings_handler(message: types.Message):
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    if not user:
        await send_error(message.chat)
    elif message.text == const.CHANGE_LANGUAGE[f'{user.lang}']:
        await send_change_language(message.chat.id, user.lang)
    elif message.text == const.BACK[f'{user.lang}']:
        await send_main_menu(user)
    else:
        await bot.send_message(message.chat.id, message.text)
