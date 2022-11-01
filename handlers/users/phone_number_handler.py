from aiogram import types
from filters.private_chat_filter import IsPrivate
from loader import dp
from states.userState import UserState
from utils.db_api.model import getUser, set_phone_number, set_phone_code, set_user_verified
from utils.misc.allmethods import send_error, get_phone_number, send_notify, send_sms, send_wrong_code, send_main_menu


@dp.message_handler(IsPrivate(), content_types=["contact"], state=UserState.contact)
@dp.message_handler(IsPrivate())
async def phone_number_handler(message: types.Message):
    user = await getUser(message.chat.id)
    phone_number = await get_phone_number(message.contact)
    if not phone_number:
        await send_error(message.chat.id)
        return
    await set_phone_number(message.from_user.id, phone_number)
    code = await send_sms(phone_number)
    await set_phone_code(message.from_user.id, code)
    await send_notify(message.chat.id, phone_number, user.lang)


@dp.message_handler(IsPrivate(), state=UserState.verification)
@dp.message_handler(IsPrivate())
async def verification_handler(message: types.Message):
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    if not user:
        await send_error(message.chat.id)
        return
    elif user.code != message.text:
        await send_wrong_code(message.chat.id, user.lang)
        return
    await set_user_verified(message.from_user.id)
    await send_main_menu(user)
