from aiogram import types
from aiogram.dispatcher.filters import filters
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter

from data.config import GROUPS
from filters.private_chat_filter import IsPrivate
from keyboards.default.all_buttons import get_back_button
from loader import dp, bot
from states.userState import UserState
from utils.db_api.model import getUser
from utils.misc.allmethods import get_branches_messages, send_error, send_main_menu, send_error_choice
from data import const_data as const
#
# @dp.message_handler(IsPrivate(),state=U)