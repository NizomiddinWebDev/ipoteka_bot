from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import const_data as const
from data.const_data import UZ


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


def get_regions_keyboard(regions, lang):
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if lang == UZ:
        rkm.add(*(KeyboardButton(region.title_uz) for region in regions))
    else:
        rkm.add(*(KeyboardButton(region.title_ru) for region in regions))
    rkm.add(KeyboardButton(const.BACK[lang]))
    return rkm


def get_products_keyboard(products, lang):
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if lang == UZ:
        rkm.add(*(KeyboardButton(product.title_uz) for product in products))
    else:
        rkm.add(*(KeyboardButton(product.title_ru) for product in products))
    rkm.add(KeyboardButton(const.BACK[lang]))
    return rkm


def get_product_text(product, lang):
    return product.description_uz if lang == UZ else product.description_ru


def get_contributions_keyboards(contribs, lang):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if lang == UZ:
        buttons.add(*(KeyboardButton(contrib.title.uz) for contrib in contribs))
    else:
        buttons.add(*(KeyboardButton(contrib.title.ru) for contrib in contribs))
    buttons.add(KeyboardButton(const.BACK[lang]))
    return buttons
