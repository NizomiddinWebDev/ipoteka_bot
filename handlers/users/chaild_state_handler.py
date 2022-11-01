from filters.private_chat_filter import IsPrivate
from loader import dp, bot
from states.userState import UserState
from utils.db_api.model import getUser
from utils.misc.allmethods import send_main_menu, send_error_choice, \
     func, child_buttons, send_dynamic_btns
from data import const_data as const


@dp.message_handler(IsPrivate(), state=UserState.child)
@dp.message_handler(IsPrivate())
async def main_menu_handler(message):
    global current
    try:
        user = await getUser(message.chat.id)
    except:
        user = None
    if message.text == const.BACK[user.lang]:

        for obj in const.response:
            if obj['id'] == current:
                current_obj = current
                if not await func(current_obj):
                    await send_main_menu(user)
                    await UserState.main_menu.set()
                else:
                    parent_id = await func(current_obj)
                    children = await child_buttons(parent_id)

                    await send_dynamic_btns(message.chat.id, user.lang, children)
                    for j in const.response:
                        if j["parent"] == parent_id:
                            current = j["id"]
                            break

                break

    for m, k in enumerate(const.response):
        if message.text == k["title"][user.lang] and k["id"] > 795:
            if k["children"]:
                for j in const.response:
                    if j["parent"] == k['id']:
                        current = j["id"]
                        break
                children = await child_buttons(k["id"])
                body = None
            else:
                children = None
                body = str(k["body"])
            await send_dynamic_btns(message.chat.id, user.lang, children, body)
            break

