from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram import F

start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message):
    # print(message.from_user)
    # await message.answer(f"Здравствуйте, {message.from_user.first_name}")

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Наш сайт', url='https://geeks.kg'),
                types.InlineKeyboardButton(text='Наш инстаграмм', url="https://www.instagram.com/_sultanbekov_05/?next=%2F")
            ],
            [
                types.InlineKeyboardButton(text='Вакансии', callback_data='jobs'),
                types.InlineKeyboardButton(text='Меню', callback_data='Menu'),
                types.InlineKeyboardButton(text='Оставьте свой отзыв', callback_data='feedback')
            ]
        ],

    )
    await message.reply(f"Добро пожаловать {message.from_user.first_name}! В наше кафе", reply_markup=kb)

@start_router.callback_query(F.data == "jobs")
async def about_us_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('В нашем кафе есть вакансии: \n1.Повар \n2.Официант \n3.SMM-специалист')


@start_router.callback_query(F.data == 'Menu')
async def menu_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Меню: \n1.Холодный напиток \n2.Блюдо')