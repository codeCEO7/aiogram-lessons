from aiogram import types

from bot.loader import dp


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}")

