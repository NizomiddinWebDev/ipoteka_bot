# from aiogram import executor
#
# from loader import dp
# import middlewares, filters, handlers
# from utils.notify_admins import on_startup_notify
# from utils.set_bot_commands import set_default_commands
#
#
# async def on_startup(dispatcher):
#     # Birlamchi komandalar (/star va /help)
#     await set_default_commands(dispatcher)
#
#     # Bot ishga tushgani haqida adminga xabar berish
#     await on_startup_notify(dispatcher)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup)

import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher.webhook import SendMessage, get_new_configured_app
from aiogram.utils import executor

# webhook settings
from data import config
from loader import bot, dp

from utils import on_startup_notify
from utils.set_bot_commands import set_default_commands

WEBHOOK_HOST = 'https://0aa9-81-95-230-194.eu.ngrok.io'
WEBHOOK_PATH = f"/app/{config.BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 8081

logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    # insert code here to run it after start


async def on_shutdown(dispatcher):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
