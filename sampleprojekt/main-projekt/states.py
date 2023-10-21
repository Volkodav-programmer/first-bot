from aiogram.fsm.state import State, StatesGroup

class Game(StatesGroup):
    first_number = State()
    second_number = State()
    game = State()
    