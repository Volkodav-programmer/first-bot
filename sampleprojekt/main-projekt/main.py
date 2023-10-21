import asyncio
import logging
import config

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram import F 

from states import Game

from game_handler import router
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер
dp = Dispatcher()
dp.include_router(router)
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f"Hello, {message.from_user.full_name}. Schreib zwei Zahlen von 1 bis 1000. Dann denke ich meine eigene Zahle zwischen diese Zahlen aus. Versuch diese Zahl zu reten.")
    await state.set_state(Game.first_number)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

