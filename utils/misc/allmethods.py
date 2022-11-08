import json
import random
import re
import requests
from aiogram.types import ReplyKeyboardMarkup
from keyboards.default import all_buttons as button
from loader import bot
from data import const_data as const
from states.userState import UserState
from .valyuta_func import get_currency
from ..db_api.model import getUser, new_user_add


async def get_by_lang(text, lang):
    try:
        ru_index = text.index('ru:')
    except:
        ru_index = 0
    try:
        uz_index = text.index('uz:')
    except:
        uz_index = 0
    if ru_index < uz_index:
        if lang == 'ru':
            return text[ru_index + 3: uz_index]
        return text[uz_index + 3:]
    if ru_index > uz_index:
        if lang == 'uz':
            return text[uz_index + 3: ru_index]
        return text[ru_index + 3:]


async def get_data_from_database():
    url = 'http://192.168.28.81:8006/api/v3/service-desk/product/for_telegram'
    response = requests.request("GET", url).json()
    with open('data/data.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, ensure_ascii=False)


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


async def check_user(chat_id, tg_user_id, full_name):
    try:
        user = await getUser(chat_id)
    except:
        user = None
    if not user:
        await new_user_add(chat_id, tg_user_id, full_name)
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


parent_in = 0
parent = 0
children = 0


async def func(obj_id):
    for obj in const.response:
        if obj['id'] == obj_id:
            for i in const.response:
                if i['id'] == obj['parent']:
                    if i["parent"] == 795:  # not i['parent']
                        return False
                    else:
                        return i['parent']


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
    await bot.send_message(user.chat_id, const.CONNECT_CONSULTANT[user.lang])

    await UserState.main_menu.set()


async def send_error(chat_id):
    await bot.send_message(chat_id, const.ERROR)
    await UserState.start.set()


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


# mobile app
async def send_mobile_app_message(chat_id, lang):
    await send_no_content(chat_id, lang)
    await bot.send_message(chat_id, f"https://play.google.com/store/apps/details?id=uz.asbt.ipoteka.mobile")


# branches
async def send_branches_message(chat_id, lang):
    global branches_list
    branches_list = []
    url = "http://dicore.uz:5005/api/v3/knowledge_base/branches/?page_size=1000"
    branches_json = requests.get(url).json()
    for branch in branches_json["results"]:
        branches_list.append({
            "id": branch['id'],
            "title": branch['title'],
            "branch_code": branch['branch_code'],
            "lng": branch['lng'],
            "lat": branch['lat'],
            "address": branch['address']
        })
    data = [branch['title'] for branch in branches_list]
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(*data)
    rkm.add(const.BACK[lang])
    await bot.send_message(chat_id, '🏦 Филиалы и банкоматы', reply_markup=rkm)
    # await bot.send_message(chat_id, const.CHOOSE[lang],
    #                        reply_markup=button.get_buttons(const.BRANCHES_MIX_KEYBOARD, lang))
    await UserState.branches.set()


async def get_branches_messages(message, chat_id):
    for branch in branches_list:
        if branch['title'] == message.text:
            text = f"{branch['address']}, {branch['id']}"
            await bot.send_message(chat_id, text)
            await bot.send_location(chat_id, branch['lng'], branch['lat'])


# settings
async def send_settings(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang], reply_markup=button.get_buttons(const.SETTINGS_KEYBOARDS, lang))
    await UserState.settings.set()


async def send_change_language(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang], reply_markup=button.get_buttons(const.LIST_LANG))
    await UserState.change_language.set()


# contact us
async def send_contact_us(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang],
                           reply_markup=button.get_buttons(const.LIST_KEYBOARDS_CONTACT_US, lang))
    await UserState.contact_us.set()


async def send_call_bank_message(chat_id, lang):
    await bot.send_message(chat_id, const.CALL_US[lang])


async def send_currency(chat_id, lang):
    text = await get_currency(lang)
    await bot.send_message(chat_id, text, parse_mode="html")


async def send_error_choice(chat_id, lang):
    await bot.send_message(chat_id, const.ERROR_CHOICE[lang])


# end function
async def send_no_content(chat_id, lang):
    await bot.send_message(chat_id, const.NO_CONTENT[lang])


async def child_buttons(parent):
    bts = [btn["title"] for btn in const.response if btn["parent"] == parent]
    return bts


async def send_dynamic_btns(chat_id, lang, children=None, body=None):
    if children:
        await bot.send_message(chat_id, const.CHOOSE[lang],
                               reply_markup=button.get_dynamic_buttons(children, lang))
    else:
        try:
            cleaner = re.compile('<p.*?>|</p.*?>|<br.*?>')
            text = re.sub(cleaner, '', body)
            text = re.sub('<strong*?>ru:</strong*?>', 'ru:', text)
            text = re.sub('<strong*?>uz:</strong*?>', 'uz:', text)
            text = await get_by_lang(text, lang)
            if text:
                await bot.send_message(chat_id, text)
            else:
                await bot.send_message(chat_id, "To'ldirilmagan")
        except Exception as e:
            print(e)


# contributions
async def send_contrib_message(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang],
                           reply_markup=button.get_buttons(const.CONTRIBUTION_KEYBOARDS, lang))
    await  UserState.contributions.set()
