from aiogram import Router, types
from aiogram.filters.command import Command


my_info_router = Router()


@my_info_router.message(Command('myinfo'))
async def my_info(message: types.Message):
    user = message.from_user
    response = (
        f"Ваш id: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваш username: @{user.username if user.username else 'Не указан'}"
    )
    await message.reply(response)