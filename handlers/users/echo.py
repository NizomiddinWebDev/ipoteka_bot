import re

from keyboards.inline.inlineData import placeInlineBtn, regionInlineBtn, countInlineBtn
from loader import bot
from aiogram.dispatcher import filters, FSMContext
from aiogram import types
from loader import dp


REGEX = f""


@dp.message_handler(text="🏡 Arenda\租赁")
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({
        "hold": "Arenda"
    })
    btn = await placeInlineBtn("Arenda")







@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def allChat(message: types.Message):
    pass



