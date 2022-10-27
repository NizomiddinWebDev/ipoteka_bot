from aiogram import types
from filters.adminFilter import IsAdmin
from filters.group_filter import IsGroup
from loader import dp, bot
from utils.db_api.model import get_user_name


@dp.message_handler(IsAdmin(), IsGroup())
async def answer_user(message: types.Message):
    if message.reply_to_message:
        print(message.reply_to_message)
        if message.reply_to_message.forward_from:
            await message.bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            try:
                user = await get_user_name(full_name=message.reply_to_message.forward_sender_name)
                await message.bot.send_message(user.tg_user_id, message.text)
            except:
                await message.answer("<b>Bu foydalanuvchining maxfiylik sozlamalari tufayli xabar yuborib bo'lmadi!</b>")
