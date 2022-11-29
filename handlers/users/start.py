from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat_filter import IsPrivate
from loader import dp
from states.adminState import AdminState
from states.userState import UserState
from utils.misc.allmethods import check_user, get_data_from_database


@dp.message_handler(IsPrivate(), CommandStart())
@dp.message_handler(IsPrivate(), CommandStart(), state=AdminState.loginState)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.child)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.change_language)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.branches)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.write_consultant)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.language)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.personal)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.contact)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.start)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.main_menu)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.settings)
@dp.message_handler(IsPrivate(), CommandStart(), state=UserState.contact_us)
async def start(message: types.Message):
    await check_user(message.chat.id, message.from_user.id, message.from_user.full_name)


@dp.message_handler(IsPrivate(), commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.child, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.main_menu, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.change_language, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.branches, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.write_consultant, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.language, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.personal, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.contact, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.start, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.settings, commands=['updatedata'])
@dp.message_handler(IsPrivate(), state=UserState.contact_us, commands=['updatedata'])
async def updates_data(message: types.Message):
    print('jdjdjd')
    try:
        await get_data_from_database()
        await message.answer("Ma'lumotlar yangilandi!")
    except:
        pass
