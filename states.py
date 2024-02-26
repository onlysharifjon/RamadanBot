# import statesgro
from aiogram.dispatcher.filters.state import StatesGroup, State


class Shogirdlar(StatesGroup):
    viloyatlar_state = State()
    iftorlik_saharlik = State()
