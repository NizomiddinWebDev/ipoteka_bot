from aiogram import types
from aiogram.dispatcher.filters import filters
from loader import dp, bot
from states.userState import UserState
from utils.db_api.model import getUser, set_user_lang
from data import const_data as const
from utils.misc.allmethods import ask_contact


@dp.message_handler(state=UserState.language)
async def language(message: types.Message):
    try:
        user = await getUser(message.chat.id)
        await message.answer("hi")
    except:
        user = None
    if not user:
        pass
    elif message.text == const.UZBEK:
        await set_user_lang(message.chat.id, const.LANG.get('uz'))
        await ask_contact(message.chat.id, const.LANG.get('uz'))
    elif message.text == const.RUSSIAN:
        await set_user_lang(message.chat.id, const.LANG.get('ru'))
        await ask_contact(message.chat.id, const.LANG.get('ru'))
    else:
        "send_error_choice(message.chat.id, user.lang)"
        pass
