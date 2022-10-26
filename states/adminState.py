from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    holdState = State()
    priceState = State()



class AdminState(StatesGroup):
    adminState = State()
    SendUsers = State()
    SendGroup = State()


class AdminPost(StatesGroup):
    holdState = State()
    placeState = State()
    viloyatState = State()
    regionState = State()
    targetState = State()
    priceState = State()
    count_roomsState = State()
    photos_idState = State()
