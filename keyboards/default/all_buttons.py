from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import const_data as const


def get_dynamic_buttons(buttons, lang=None, n=2):
    rkm = ReplyKeyboardMarkup(row_width=n, resize_keyboard=True)
    if lang is None:
        rkm.add(*(KeyboardButton(btn) for btn in buttons))
    else:
        rkm.add(*(KeyboardButton(btn[lang]) for btn in buttons))
        rkm.add(KeyboardButton(const.BACK[lang]))
    return rkm


def get_buttons(buttons, lang=None, n=2):
    rkm = ReplyKeyboardMarkup(row_width=n, resize_keyboard=True)
    if lang is None:
        rkm.add(*(KeyboardButton(btn) for btn in buttons))
    else:
        rkm.add(*(KeyboardButton(btn[lang]) for btn in buttons))
    return rkm


def get_phone_number_button(lang):
    return ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
        KeyboardButton(const.ASK_PHONE_NUMBER[lang], request_contact=True),
    )


def get_main_menu_keyboard(lang):
    rkm = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    rkm.add(*(KeyboardButton(btn[lang]) for btn in const.MAIN_MENU_KEYBOARD))
    rkm.add(KeyboardButton(const.CONTACT_US[lang]))
    return rkm


def get_remove_keyboard():
    return ReplyKeyboardRemove()
