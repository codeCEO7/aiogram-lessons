from aiogram import types

from bot.loader import dp
from bot.utils.db_api.db_quick_commands import select_user


@dp.message_handler(commands=['profile'])
async def show_profile(message: types.Message):
    user = select_user(message.from_user.id)

    await message.answer(f"Твой профиль📌\n"
                         f"Name: {user.name}\n"
                         f"Username: @{user.username}\n"
                         f"Admin: {'Да' if user.admin else 'Нет'}")