from aiogram.dispatcher.router import Router
from aiogram.fsm.context import FSMContext   
from aiogram.types import Message
from aiogram import F 

from random import randint

from states import Game

router = Router()

@router.message(Game.first_number)
async def first_number(message: Message, state: FSMContext):
    if message.text.isnumeric():
        if int(message.text) > 1000 or int(message.text) < 0:
            await message.answer("HUI")
            return
        await message.answer("Ok. Schreib zweite Zahl.")
        await state.set_data({'first_number':int(message.text)})
        await state.set_state(Game.second_number)
    else:
        await message.answer("Deine Nachricht ist keine Zahl. Versuch noch mal.")

@router.message(Game.second_number)
async def second_number(message: Message, state: FSMContext):
    if message.text.isnumeric():
        if int(message.text) > 1000 or int(message.text) < 0:
            await message.answer("HUI")
            return

        first_number1 = (await state.get_data())['first_number']
        if int(message.text) < first_number1:
            await message.answer("AGain HUI")
            await state.set_state(Game.first_number)
            return
        await state.set_data({'my_number':randint(first_number1, int(message.text))})
        await message.answer("Ok. Lass uns das Spiel anfangen. Versuch meine Zahle zu reten")
        await state.set_state(Game.game)
    else:
        await message.answer("Deine Nachricht ist keine Zahl. Versuch noch mal.")
    
@router.message(Game.game)
async def game(message: Message, state: FSMContext):
    data = await state.get_data()
    my_number = data['my_number']

    if message.text.isnumeric():
        user_number = int(message.text)
        if user_number == my_number:
            await message.answer('Ich gratuliere dich. Du hast geretet!')
            await state.set_state()
        elif user_number < my_number:
            await message.answer('Deine Zahl ist weniger als meine')
        else:
            await message.answer("Deine Zahl ist großer als meine")
    else:
        await message.answer('Schreib die Zahl bitte.') 