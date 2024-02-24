from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    calc = State()
    start = State()
    end_calc = State()
    
    
class Order(StatesGroup):
    fullname = State()
    address = State()
    size = State()
    price = State()
    link = State()
    end_order = State()