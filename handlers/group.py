from AllHomework.bot_config import group

from aiogram import Router, F, types
from aiogram.filters.command import Command
from AllHomework.bot_config import Bot, bot
from datetime import timedelta
from profanity_check import predict_prob

group_router = Router()

BAD_WORDS = ("тупой", "дурак", "дебил, говнюк, ублюдок")


@group_router.message(Command('ban', prefix="!"))
async def ban_user(message: types.Message):
    print(message.text)
    reply = message.reply_to_message
    print("Reply or not", reply)
    if reply:
        author = reply.from_user.id
        await bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=author,
            until_date=timedelta(seconds=60)
        )

@group_router.message(lambda m:m.chat.id==int(group))
async def filter_bad_words(message: types.Message):
    for word in BAD_WORDS:
        if word in message.text.lower():
            await message.delete()
            await message.answer(
                f'Do not swear {message.from_user.first_name}'
            )