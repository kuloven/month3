from month3.bot_config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command
import random
from aiogram.types import FSInputFile
from profanity_check import predict_prob
from month3.bot_config import group


group_router = Router()


@group_router.message()
async def group_handler(message: types.Message):
    if message.chat.id == int(group):
        badness = predict_prob([message.text])
        print(badness)
        if badness[0] >= 0.6:
            await message.delete()
            await bot.send_message(
                chat_id=int(group),
                text=f'user: {message.from_user.first_name} u have written bad word!!!!!'
            )
            await bot.ban_chat_member(chat_id=int(group), user_id=message.from_user.id)