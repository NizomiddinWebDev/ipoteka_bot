from aiogram import types
from data.config import GROUPS
from filters.private_chat_filter import IsPrivate
from keyboards.default.all_buttons import get_back_button
from loader import dp, bot
from states.userState import UserState
from utils.db_api.model import getUser
from utils.misc.allmethods import send_error, send_call_bank_message, send_main_menu, send_error_choice, send_contact_us
from data import const_data as const


@dp.message_handler(IsPrivate(), state=UserState.contact_us)
@dp.message_handler(IsPrivate())
async def contact_us_handler(message: types.Message):
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    if not user:
        await send_error(message.chat.id)
    elif message.text == const.CALL_BANK[user.lang]:
        await send_call_bank_message(message.chat.id, user.lang)
    elif message.text == const.WRITE_CONSULTANT[user.lang]:
        await message.answer(const.WRITE_FEEDBACK[user.lang], reply_markup=get_back_button(user.lang))
        await UserState.write_consultant.set()
    elif message.text == const.BACK[user.lang]:
        await send_main_menu(user)
    else:
        await send_error_choice(message.chat.id, user.lang)


@dp.message_handler(IsPrivate(),
                    content_types=['audio', 'document', 'text', 'photo', 'sticker', 'video', 'voice', 'contact',
                                   'location'],
                    state=UserState.write_consultant)
async def write_consultant(message: types.Message):
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    if not user:
        await send_error(message.chat.id)
    else:
        if message.text == const.BACK[user.lang]:
            await send_contact_us(message.from_user.id, user.lang)
        else:
            await message.forward(GROUPS[0])
            await message.answer(const.THANKS_FEEDBACK[user.lang])
