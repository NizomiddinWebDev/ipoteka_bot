from aiogram import types
from filters.adminFilter import IsAdmin
from filters.group_filter import IsGroup
from loader import dp, bot
from utils.db_api.model import get_user_name, ban_user, unban_user


@dp.message_handler(IsGroup(), commands=['ban'])
async def answer_user(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.forward_from:
            try:
                await ban_user(message.reply_to_message.forward_from.id)
                await message.answer(f"<a href='tg://user?id={message.reply_to_message.forward_from.id}'>{message.reply_to_message.forward_sender_name}</a> 1 oyga yozish huquqidan mahrum qildingiz!")
                await message.bot.send_message(message.reply_to_message.forward_from.id, "Siz admin tomonidan 1 oy "
                                                                                         "mudatga yozish huquqidan "
                                                                                         "mahrum qilindingiz!")
            except:
                await message.answer("Xatolik yuz berdi!")
        else:
            try:
                user = await get_user_name(full_name=message.reply_to_message.forward_sender_name)
                await ban_user(user.tg_user_id)
                await message.answer(f"<a href='tg://user?id={user.tg_user_id}'>{message.reply_to_message.forward_sender_name}</a> 1 oyga yozish huquqidan mahrum qildingiz!")
                await message.bot.send_message(user.tg_user_id,
                                               "Siz admin tomonidan 1oy mudatga yozish huquqidan mahrum qilindingiz!")
            except:
                await message.answer(
                    "<b>Bu foydalanuvchining Maxfiylik sozlamalari tufayli Banga solib bolmadi!</b>")


@dp.message_handler(IsGroup(), commands=['unban'])
async def answer_user(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.forward_from:
            try:
                await unban_user(message.reply_to_message.forward_from.id)
                await message.answer("Foydalanuvchi bandan olindi!")
                await message.bot.send_message(message.reply_to_message.forward_from.id, "Siz Bandan olindingiz! "
                                                                                         "murojat yo'llashingiz "
                                                                                         "mumkin!")
            except:
                await message.answer("Xatolik yuz berdi!")
        else:
            try:
                user = await get_user_name(full_name=message.reply_to_message.forward_sender_name)
                await unban_user(user.tg_user_id)
                await message.answer("Foydalanuvchi bandan olindi!")
                await message.bot.send_message(user.tg_user_id, "Siz Bandan olindingiz! murojat yo'llashingiz mumkin!")
            except:
                await message.answer(
                    "<b>Bu foydalanuvchining Maxfiylik sozlamalari tufayli bandan olib bolmadi!</b>")


@dp.message_handler(IsGroup())
async def answer_user(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.forward_from:
            await message.bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            try:
                user = await get_user_name(full_name=message.reply_to_message.forward_sender_name)
                await message.bot.send_message(user.tg_user_id, message.text)
            except:
                await message.answer(
                    "<b>Bu foydalanuvchining Maxfiylik sozlamalari tufayli xabar yuborib bo'lmadi!</b>")
