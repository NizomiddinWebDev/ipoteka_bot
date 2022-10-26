from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.model import get_place, get_region, get_regionCount, getCountRooms


async def placeInlineBtn(hold):
    hold = await get_place(hold)
    markup = InlineKeyboardMarkup(row_width=2)
    for i in hold:
        markup.insert(
            InlineKeyboardButton(text=i[0], callback_data=i[0])
        )
    return markup


async def regionInlineBtn(hold, place):
    region = await get_region(hold=hold, place=place)
    markup = InlineKeyboardMarkup(row_width=2)
    for i in region:
        count = await get_regionCount(hold, place, i[0])
        markup.insert(
            InlineKeyboardButton(text=f"{i[0]} {count} ta", callback_data=i[0])
        )
    markup.insert(InlineKeyboardButton(text="🔙 ortga", callback_data="ortga"))
    return markup


async def countInlineBtn(hold, place, region):
    count_room = await getCountRooms(hold=hold, place=place, region=region)
    markup = InlineKeyboardMarkup(row_width=2)
    for i in count_room:
        markup.insert(InlineKeyboardButton(text=f"{i[0]}", callback_data=i[0]))
    return markup
