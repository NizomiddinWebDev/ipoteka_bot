from aiogram import types
from filters.private_chat_filter import IsPrivate
from loader import dp
from states.userState import UserState
from utils.db_api.model import getUser
from data import const_data as const
from utils.misc.allmethods import send_error, \
    send_currency, send_mobile_app_message, send_branches_message, send_settings, \
    send_contact_us, send_error_choice, child_buttons, send_dynamic_btns, send_main_menu


@dp.message_handler(IsPrivate(), state=UserState.main_menu)
@dp.message_handler(IsPrivate())
async def main_menu_handler(message: types.Message):
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    if not user:
        await send_error(message.chat.id)
    elif message.text == const.COURSE_CURRENCY[user.lang]:
        await send_currency(message.chat.id, user.lang)
    elif message.text == const.MOBILE_APP[user.lang]:
        await send_mobile_app_message(message.chat.id, user.lang)
    elif message.text == const.BRANCHES_N_MINIBANKS[user.lang]:
        await send_branches_message(message.chat.id, user.lang)
    elif message.text == const.SETTINGS[user.lang]:
        await send_settings(message.chat.id, user.lang)
    elif message.text == const.CONTACT_US[user.lang]:
        await send_contact_us(message.chat.id, user.lang)
    elif True:
        for m, k in enumerate(const.MAIN_BTNS):
            if message.text == k[user.lang]:
                for i in const.response:
                    if i["title"][user.lang] == message.text and i["id"] > 795:
                        global current
                        if i["children"]:
                            for j in const.response:
                                if j["parent"] == i['id']:
                                    current = j["id"]
                                    break
                            children = await child_buttons(i["id"])
                            body = None
                        else:
                            children = None
                            body = str(i["body"])
                await send_dynamic_btns(message.chat.id, user.lang, children, body)
                await UserState.child.set()
            elif message.text == const.BACK[user.lang]:
                await send_main_menu(user)
                break

    else:
        await send_error_choice(message.chat.id, user.lang)
