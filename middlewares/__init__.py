# from aiogram import Dispatcher


from aiogram.contrib.middlewares.logging import LoggingMiddleware

from loader import dp
from .checkedMiddleware import BigBrother
from .throttling import ThrottlingMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())

    # dp.middleware.setup(BigBrother())
