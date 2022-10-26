import json
import random

import requests

from keyboards.default import all_buttons as button
from loader import bot
from data import const_data as const
from states.userState import UserState
from ..db_api.model import getUser, new_user_add


async def check_phone_number(phone_number):
    if phone_number and len(phone_number) == 12 and phone_number.isdecimal() and phone_number.startswith("998"):
        return True
    return False


async def get_phone_number(contact):
    if not (contact and contact.phone_number):
        return None
    if "+" in contact.phone_number:
        return contact.phone_number[1:]
    return contact.phone_number[1:]


async def check_user(chat_id, tg_user_id):
    try:
        user = await getUser(chat_id)
    except:
        user = None
    if not user:
        await new_user_add(chat_id, tg_user_id)
        await send_welcome(chat_id)
        await ask_language(chat_id)
    elif not user.lang:
        await ask_language(chat_id)
    elif not user.phone_number:
        await ask_contact(chat_id, user.lang)
    elif not user.is_verified:
        await send_notify(chat_id, user.phone_number, user.lang)
    elif user.is_verified:
        await send_main_menu(user)
    else:
        pass


# Send message

# start
async def send_welcome(chat_id):
    await bot.send_message(chat_id, const.WELCOME_MESSAGE)


# register
async def ask_language(chat_id):
    await bot.send_message(chat_id, const.ASK_LANGUAGE, reply_markup=button.get_buttons(const.LIST_LANG))
    await UserState.language.set()


async def ask_contact(chat_id, lang):
    await bot.send_message(chat_id, const.ASK_PHONE_NUMBER[lang], reply_markup=button.get_phone_number_button(lang))
    await UserState.contact.set()


async def send_notify(chat_id, phone_number, lang):
    await bot.send_message(chat_id, const.SENT_NOTIFY[lang].format(phone_number=phone_number),
                           reply_markup=button.get_remove_keyboard())
    await UserState.verification.set()


async def send_wrong_code(chat_id, lang):
    await bot.send_message(chat_id, const.WRONG_CODE[lang])


async def send_phone_number_not_found(chat_id, lang):
    await bot.send_message(chat_id, const.WRONG_PHONE_NUMBER[lang])


async def send_main_menu(user):
    await bot.send_message(user.chat_id, const.MAIN_MENU[user.lang],
                           reply_markup=button.get_main_menu_keyboard(user.lang))
    await UserState.main_menu.set()


async def send_error(chat_id):
    await bot.send_message(chat_id, const.ERROR)
    UserState.start.set()


async def send_sms(phone):
    phone = phone[-9:: 1]
    url = "http://91.204.239.44/broker-api/send"
    # url = "http://91.204.239.44:2775/broker-api/send"
    _code = random.randint(1000, 9999)
    payload = json.dumps({
        "messages": [
            {
                "recipient": '998' + phone,
                "message-id": 'sd' + str(_code),
                "sms": {
                    "originator": "1600",
                    "content": {
                        "text": _code
                    }
                }
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic aXBvdGVrYWJhbms5OnRmNTVONllr'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return _code
    else:
        pass