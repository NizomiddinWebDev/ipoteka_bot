from aiogram import types
from filters.private_chat_filter import IsPrivate
from loader import dp
from states.userState import UserState
from utils.db_api.model import getUser
from utils.misc.allmethods import get_branches_messages, send_error, send_main_menu, send_error_choice
from data import const_data as const


@dp.message_handler(IsPrivate(), state=UserState.branches)
@dp.message_handler(IsPrivate())
async def branches(message: types.Message):
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    await get_branches_messages(message, message.chat.id)
    if not user:
        await send_error(message.chat)
    elif message.text == const.BACK[user.lang]:
        await send_main_menu(user)
    elif not message:
        await send_error_choice(message.chat.id, user.lang)
