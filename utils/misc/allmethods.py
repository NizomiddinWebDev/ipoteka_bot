import json
import random

import requests
from aiogram.types import ReplyKeyboardMarkup

from data.const_data import FROM_OFFICE, FROM_MOBILE, PERSONAL
from keyboards.default import all_buttons as button
from keyboards.default.all_buttons import get_buttons
from loader import bot
from data import const_data as const
from states.userState import UserState
from .valyuta_func import get_currency
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

# personal
async def send_personal_message(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang], reply_markup=button.get_buttons(const.PERSONAL_KEYBOARDS, lang))
    await UserState.personal.set()


async def send_personal_source_deposit_message(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang],
                           reply_markup=button.get_buttons(const.PERSONAL_DEPOSIT_SOURCE_KEYBOARD, lang))
    await UserState.personal_deposit_source.set()


async def send_personal_currency_deposit_message(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang],
                           reply_markup=button.get_buttons(const.PERSONAL_CURRENCY_KEYBOARD, lang))
    await UserState.personal_deposit_currency.set()


async def send_deposits(chat_id, lang, state, currency):
    source = FROM_OFFICE if state == UserState.personal_deposit_bank else FROM_MOBILE
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=button.get_products_keyboard(db_utils.get_deposits(PERSONAL, source, currency), lang))
    bot.set_state(chat_id, state)


def send_deposit(chat_id, lang, deposit):
    bot.send_message(chat_id, utils.get_product_text(deposit, lang))


def send_credit_type(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang], reply_markup=button.get_buttons(const.CREDIT_TYPE_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.personal_credit_type)


# credits inner consumer credit categories side

def send_personal_credit_consumer(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.PERSONAL_CONSUMER_CREDITS, lang))
    bot.set_state(chat_id, UserState.personal_consumer_credit)


def send_personal_consumer_credit_online_mikrozime(chat_id, lang):
    bot.send_message(chat_id, const.CONSUMER_CREDIT_ONLINE_MIKROZIME_MSG[lang])


def send_personal_consumer_credit_message(chat_id, lang):
    bot.send_message(chat_id, const.CONSUMER_CREDIT_MSG[lang])


def send_personal_ipo_credit_message(chat_id, lang):
    bot.send_message(chat_id, const.IPO_CREDIT_MSG[lang], parse_mode="HTML")


def send_credit_consumer_credit_mikrozime(chat_id, lang):
    bot.send_message(chat_id, const.CONSUMER_CREDIT_MIKROZIME_MSG[lang], parse_mode='HTML')


def send_credit_consumer_credit_online_mikrozime(chat_id, lang):
    bot.send_message(chat_id, const.CONSUMER_CREDIT_ONLINE_MIKROZIME_MSG[lang], parse_mode='HTML')


def send_credit_consumer_study(chat_id, lang):
    bot.send_message(chat_id, const.CONSUMER_STUDY_MSG[lang])


def send_credit_consumer_credit_simple(chat_id, lang):
    bot.send_message(chat_id, const.CONSUMER_CREDIT_MSG[lang], parse_mode='HTML')


def send_credit_fadin(chat_id, lang):
    bot.send_message(chat_id, const.FADIN_MSG[lang], parse_mode='HTML')


def send_credit(chat_id, lang, credit):
    bot.send_message(chat_id, utils.get_product_text(credit, lang))


def send_card_currency(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.PERSONAL_CURRENCY_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.personal_card_currency)


def send_cards(chat_id, lang, currency):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_products_keyboard(db_utils.get_cards(PERSONAL, currency), lang))
    bot.set_state(chat_id, UserState.personal_card)


def send_card(chat_id, lang, card):
    bot.send_message(chat_id, utils.get_product_text(card, lang))


def send_money_transfers(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.MONEY_TRANSFERS_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.money_transfers)


# money_gram side
def send_money_gram(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.MONEY_GRAM_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.money_transfers_moneygram)


def send_money_gram_mix_message(chat_id, lang):
    bot.send_message(chat_id, const.MONEY_GRAM_MIX_MSG[lang], parse_mode='HTML')


def send_money_gram_russia_message(chat_id, lang):
    bot.send_message(chat_id, const.MONEY_GRAM_CENTRAL_RUSSIA_MSG[lang], parse_mode='HTML')


def send_money_gram_china_message(chat_id, lang):
    bot.send_message(chat_id, const.MONEY_GRAM_CHINA_MSG[lang], parse_mode='HTML')


def send_money_gram_ukrain_message(chat_id, lang):
    bot.send_message(chat_id, const.MONEY_GRAM_UKRAIN_MSG[lang], parse_mode='HTML')


def send_money_gram_all_message(chat_id, lang):
    bot.send_message(chat_id, const.MONEY_GRAM_ALL_MSG[lang], parse_mode='HTML')


# money transfers contact
def send_money_transfers_contact(chat_id, lang):
    bot.send_message(chat_id, const.MONEY_TRANSFERS_CONTACT_FIRST[lang])
    bot.send_message(chat_id, const.MONEY_TRANSFERS_CONTACT_SECOND[lang])
    # bot.send_message(chat_id, const.CHOOSE[lang],
    #                  reply_markup=utils.get_buttons(const.MONEY_TRAMSFERS_CONTACT_KEYBOARD, lang))
    # bot.set_state(chat_id, UserState.money_transfers_contact)


def send_money_transfers_first(chat_id, lang):
    bot.send_message(chat_id, const.NO_CONTENT[lang])


def send_money_transfers_second(chat_id, lang):
    bot.send_message(chat_id, const.NO_CONTENT[lang])


# corporate
async def send_corporate_message(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang],
                           reply_markup=button.get_buttons(const.LIST_CORPORATE_KEYBOARDS, lang))
    await UserState.corporate.set()


# entrepreneur
async def send_entrepreneur_message(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang], reply_markup=button.get_buttons(const.LIST_ENTREPRENEURS, lang))
    await UserState.entrepreneur.set()


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
    print(len(data))
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(*data)
    rkm.add(const.BACK[lang])
    await bot.send_message(chat_id, '🏦 Филиалы и банкоматы', reply_markup=rkm)
    # await bot.send_message(chat_id, const.CHOOSE[lang],
    #                        reply_markup=button.get_buttons(const.BRANCHES_MIX_KEYBOARD, lang))
    await UserState.branches.set()


async def get_branches_messages(message, chat_id):
    for branch in branches_list:
        print(len(branch))
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
        # print(body)
        await bot.send_message(chat_id, body, parse_mode='html')


# contributions
async def send_contrib_message(chat_id, lang):
    await bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=button.get_buttons(const.CONTRIBUTION_KEYBOARDS, lang))
    await bot.set_state(chat_id, UserState.contributions)


# contributions - via bank

def send_contrib_via_bank_message(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.CONTRIBUTION_VIA_BANK_KEYBOARDS, lang))
    bot.set_state(chat_id, UserState.contributions_via_bank)


# contributions - via mobile
def send_contrib_via_mobile_message(chat_id, lang):
    bot.send_message(chat_id, const.VIA_MOBILE_CONTRIBUTION[lang], parse_mode='HTML',
                     reply_markup=utils.get_buttons(const.VIA_MOBILE_CONTRIBUTION_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.contributions_via_mobile)


# contributions - via bank - via nationan and internation currency
def send_contrib_via_national_currency_message(chat_id, lang):
    bot.send_message(chat_id, const.VIA_NATIONAL_CURRENCY[lang], parse_mode='HTML')


# money transfers - categories
# def send_money_transfers_categories(chat_id, lang):
def send_money_transfers_types(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.MONEY_TRANSFERS_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.money_transfers)


# money transfers
# western inner functions
def send_money_transfers_western_types(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.WESTERN_UNION_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.money_transfers_western)


def send_money_transfers_western_central_asia_msg(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang], parse_mode='HTML',
                     reply_markup=utils.get_buttons(const.WESTERN_CENTRAL_ASIA_KEYBOARD, lang))
    bot.set_state(chat_id, UserState.money_transfers_western_central_asia)


def send_money_transfers_western_central_asia_special_msg(chat_id, lang):
    bot.send_message(chat_id, const.WESTERN_CENTRAL_ASIA_SPECIAL_MSG[lang], parse_mode='HTML')


def send_money_transfers_western_central_asia_twelwe_hours_msg(chat_id, lang):
    bot.send_message(chat_id, const.WESTERN_CENTRAL_ASIA_TWELWE_HOURS_MSG[lang], parse_mode='HTML')


def send_money_transfers_western_china_msg(chat_id, lang):
    bot.send_message(chat_id, const.WESTERN_CHINA_MSG[lang], parse_mode='HTML')


def send_money_transfers_western_oae(chat_id, lang):
    bot.send_message(chat_id, const.WESTERN_OAE_MSG[lang], parse_mode='HTML')


def send_money_transfers_western_all_countries(chat_id, lang):
    bot.send_message(chat_id, const.WESTERN_ALL_COUNTRIES_MSG[lang], parse_mode='HTML')


# OAE types and all
def send_money_transfers_western_oae_types(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.WESTERN_UNION_KEYBOARD, lang), parse_mode='HTML')
    bot.set_state(chat_id, UserState.money_transfers_western)


# golden crone
# zolataya korona msg

def send_unistream_msg(chat_id, lang):
    bot.send_message(chat_id, const.UNISTREAM_MSG[lang], parse_mode='HTML')


def send_ria_msg(chat_id, lang):
    bot.send_message(chat_id, const.RIA_MSG[lang], parse_mode='HTML')


def send_money_transfers_golden_crone(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.GOLDEN_CRONE_KEYBOARD, lang))
    bot.send_message(chat_id, const.GOLDEN_CRONE_FREE[lang], parse_mode='HTML')
    bot.set_state(chat_id, UserState.money_transfers_golden_crone)


def send_money_transfers_golden_crone_asia_message(chat_id, lang):
    bot.send_message(chat_id, const.GOLDEN_CRONE_ASIA_MSG[lang], parse_mode='HTML')


def send_money_transfers_golden_crone_europe_message(chat_id, lang):
    bot.send_message(chat_id, const.GOLDEN_CRONE_EUROPE_MSG[lang], parse_mode='HTML')


def send_money_transfers_golden_crone_central_asia_msg(chat_id, lang):
    bot.send_message(chat_id, const.GOLDEN_CRONE_CENTRAL_ASIA_MSG[lang], parse_mode='HTML')


def send_money_transfers_golden_crone_china_message(chat_id, lang):
    bot.send_message(chat_id, const.GOLDEN_CRONE_CHINA_MSG[lang], parse_mode='HTML')


def send_money_transfers_golden_crone_korea(chat_id, lang):
    bot.send_message(chat_id, const.GOLDEN_CRONE_KOREA_MSG[lang], parse_mode='HTML')


def send_money_transfers_paysend_msg(chat_id, lang):
    bot.send_message(chat_id, const.PAYSEND_MSG[lang], parse_mode='HTML')


# money transfers asia express side
def bot_send_asia_express(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.MONEY_TRANSFERS_ASIA_EXPRESS_KEYBOARD, lang),
                     parse_mode='HTML')
    bot.set_state(chat_id, UserState.money_transfers_asia_express)


def send_money_transfers_asia_express_message(chat_id, lang):
    bot.send_message(chat_id, const.MONEY_TRANSFERS_ASIA_EXPRESS_MSG[lang], parse_mode='HTML')


async def send_contrib_via_internation_currency_message(chat_id, lang):
    bot.send_message(chat_id, const.VIA_INTERNATION_CURRENCY[lang], parse_mode='HTML')


# cards

async def send_personal_national_cards(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.NATIONAL_CURRENCY_CARDS, lang), parse_mode='HTML')
    bot.set_state(chat_id, UserState.personal_national_card)


async def send_personal_national_uzcard_message(chat_id, lang):
    bot.send_message(chat_id, const.UZCARD_CARD_MSG[lang], parse_mode='HTML')


async def send_personal_national_humo_message(chat_id, lang):
    bot.send_message(chat_id, const.HUMO_CARD_MSG[lang], parse_mode='HTML')


async def send_personal_internation_cards(chat_id, lang):
    bot.send_message(chat_id, const.CHOOSE[lang],
                     reply_markup=utils.get_buttons(const.INTERNATION_CURRENCY_CARDS, lang))
    bot.set_state(chat_id, UserState.personal_internation_card)


async def send_personal_internation_mastercard_standart_message(chat_id, lang):
    bot.send_message(chat_id, const.MASTERCARD_STANDART_CARD_MSG[lang], parse_mode='HTML')


async def send_personal_internation_mastercard_gold_message(chat_id, lang):
    bot.send_message(chat_id, const.MASTERCARD_GOLD_CARD_MSG[lang], parse_mode='HTML')


# etc
async def send_currency(chat_id, lang):
    bot.send_message(chat_id, utils.get_currency(lang), parse_mode="html")


async def send_error(chat_id):
    bot.send_message(chat_id, const.ERROR)
    bot.set_state(chat_id, UserState.start)


async def send_error_choice(chat_id, lang):
    bot.send_message(chat_id, const.ERROR_CHOICE[lang])


async def send_no_content(chat_id, lang):
    bot.send_message(chat_id, const.NO_CONTENT[lang])
