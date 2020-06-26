from aiogram.dispatcher.filters.state import State, StatesGroup

class Parametrs(StatesGroup):
    default = State()
    waiting_for_height = State()
    waiting_for_weight = State()
