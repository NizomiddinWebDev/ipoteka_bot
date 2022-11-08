import logging

from aiogram.utils import executor
from handlers import *

from utils import on_startup_notify
from utils.set_bot_commands import set_default_commands

WEBHOOK_HOST = 'https://6477-81-95-230-194.eu.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 8081

logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)
    await set_default_commands(dispatcher)

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
