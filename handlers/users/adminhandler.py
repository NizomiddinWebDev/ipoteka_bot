import os
from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS, ADMIN_PASSWORD
from filters.private_chat_filter import IsPrivate
from keyboards.default.adminKeyboard import adminButton, back
from loader import dp
from states.adminState import AdminState
from states.userState import UserState
from utils.db_api.model import getUserList, getUsersCount
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands='admin')
@dp.message_handler(IsPrivate(), state=UserState.child, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.main_menu, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.change_language, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.branches, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.write_consultant, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.language, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.personal, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.contact, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.start, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.settings, commands=['admin'])
@dp.message_handler(IsPrivate(), state=UserState.contact_us, commands=['admin'])
async def admin_panel(msg: types.Message):
    user_id = msg.from_user.id
    if os.stat("data/admin/admin.txt").st_size == 0:
        await msg.reply("<b>Siz noto'g'ri buyruq kiritdingiz!</b>")
        return
    f = open('data/admin/admin.txt', 'r')
    read = f.read()
    read = read.split('\n')
    f.close()
    if str(user_id) in read:
        await msg.reply(f"{msg.from_user.full_name} Admin panelga hush kelibsiz!", reply_markup=adminButton)
        await AdminState.adminState.set()
    else:
        await msg.reply("<b>Admin panelga o'tish uchun parolni kiriting!</b>")
        await AdminState.loginState.set()


@dp.message_handler(state=AdminState.loginState, content_types=['text'])
async def login_handler(msg: types.Message, state: FSMContext):
    if msg.text == ADMIN_PASSWORD:
        admin = msg.from_user.id
        f = open('data/admin/admin.txt', 'a')
        f.write(f"{admin}\n")
        f.close()
        await msg.answer("<b>Yangi Admin muvafaqiyatli qo'shildi✅</b>")
        await msg.reply(f"{msg.from_user.full_name} Admin panelga hush kelibsiz!", reply_markup=adminButton)
        await AdminState.adminState.set()
    else:
        await msg.answer("<b>Parol xato kiritildi! qaytadan urinib ko'ring!</b>")


@dp.message_handler(text="Send Users", state=AdminState.adminState)
async def send_users(msg: types.Message):
    await AdminState.next()
    await msg.reply("Userlarga yuboriladigan habarni kiriting!", reply_markup=back)


@dp.message_handler(text="Statistic", state=AdminState.SendUsers)
@dp.message_handler(text="Statistic", state=AdminState.adminState)
async def user_statistic(msg: types.Message):
    rowsUser = await getUsersCount()
    await msg.answer(f"<b>📊 Bot Statistikasi \n\n 👤 Members: {rowsUser}\n👥 Groups: {1}</b>")


@dp.message_handler(state=AdminState.adminState, text="🔙exit")
@dp.message_handler(state=AdminState.SendUsers, text="🔙exit")
async def exit_admin(msg: types.Message, state: FSMContext):
    await msg.answer("Exit", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(state=AdminState.SendUsers, text="🔙ortga")
async def exit_admin(msg: types.Message, state: FSMContext):
    await msg.answer("Orga qaytildi", reply_markup=adminButton)
    await AdminState.adminState.set()


@dp.message_handler(state=AdminState.SendUsers, content_types=types.ContentTypes.ANY)
async def send_users(msg: types.Message):
    reply_markup = msg.reply_markup
    rows = await getUserList()
    count = 0
    for row in rows:
        try:
            await msg.bot.copy_message(row.tg_user_id, msg.from_user.id, msg.message_id, reply_markup=reply_markup)
            count += 1
        except:
            pass
        await sleep(0.5)
    await msg.reply(f"{count} ta foydalanuvchilarga habar yuborildi")
