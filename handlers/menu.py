from aiogram import Router, F, types
from aiogram.filters.command import Command
from AllHomework.bot_config import database
from aiogram.types import FSInputFile

menu_router = Router()

@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Холодный напиток', callback_data='drinks'),
                types.InlineKeyboardButton(text='Первое блюдо', callback_data='first'),
                types.InlineKeyboardButton(text='Второе блюдо', callback_data='second')
            ]
        ]
    )
    await message.answer('Выберите что-нибудь из категорий:', reply_markup=kb)

signal = ('drinks', 'first', 'second')

@menu_router.callback_query(lambda call:call.data in signal)
async def dishes(call: types.CallbackQuery):
    query = """
    SELECT * FROM dishes JOIN category_dishes ON dishes.category_of_dishes_id = category_dishes.id WHERE category_dishes.name = ?
    """
    data = database.fetch(
        query=query,
        params=(call.data,)
    )
    # print(data)
    for i in data:
        photo = FSInputFile(i[3])
        await call.message.answer_photo(photo=photo, caption=f'name: {i[1]}\n'
                                                             f'price: {i[2]}')