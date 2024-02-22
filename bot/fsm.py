from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    calc = State()
    start = State()
    end_calc = State()
    address = State()
    fullname = State()
    size = State()
    price = State()
    link = State()
    photo_id = State()