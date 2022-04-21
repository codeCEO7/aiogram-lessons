from aiogram import types

from bot.loader import dp
from bot.utils.db_api.db_quick_commands import register_user


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user = register_user(message)

    if user:
        await message.answer('Вы успешно зарегистрировались!')
    else:
        await message.answer('Вы уже зарегистрированы!')

