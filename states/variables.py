from telebot.handler_backends import State, StatesGroup


class Variables(StatesGroup):
    min_price = State()
    max_price = State()
    start_price = State()
    end_price = State()
    date_to = State()
    date_from = State()
    aero_from = State()
    aero_to = State()
