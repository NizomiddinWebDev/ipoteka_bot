from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    holdState = State()
    priceState = State()


class AdminState(StatesGroup):
    adminState = State()
    SendUsers = State()
    SendGroup = State()
