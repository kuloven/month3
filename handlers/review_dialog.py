import re
from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from AllHomework.bot_config import database
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

review_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.callback_query(F.data == 'feedback')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await call.message.answer('Как вас зовут?')


@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    if not name.isalpha():
        await message.answer('Вводите только буквы')
        return
    await state.update_data(name=name)
    await state.set_state(RestourantReview.instagram_username)
    await message.answer('Ваш инстаграмм профиль?')


@review_router.message(RestourantReview.instagram_username)
async def process_instagram_username(message: types.Message, state: FSMContext):
    await state.update_data(instagram_username=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Пожалуйста, введите дату вашего посещения (ДД.ММ.ГГ):")


@review_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    visit_date = message.text
    if not re.match(r'^\d{2}\.\d{2}\.\d{2}$', visit_date):
        await message.answer('Введите дату в формате ДД.ММ.ГГ')
        return
    await state.update_data(visit_date=visit_date)
    await state.set_state(RestourantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='1'), types.KeyboardButton(text='2'), types.KeyboardButton(text='3')],
            [types.KeyboardButton(text='4'), types.KeyboardButton(text='5')]
        ],
        resize_keyboard=True
    )
    await message.answer('Как оцениваете качество еды? \n (1 - Очень плохо, 2 - Плохо, 3 - Нормально,'
                         ' 4 - Хорошо, 5 - Отлично)', reply_markup=kb)


@review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    food_rating = message.text
    if food_rating not in ['1', '2', '3', '4', '5']:
        await message.answer('Пожалуйста, выберите рейтинг от 1 до 5')
        return
    await state.update_data(food_rating=food_rating)
    await state.set_state(RestourantReview.cleanliness_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='1'), types.KeyboardButton(text='2'), types.KeyboardButton(text='3')],
            [types.KeyboardButton(text='4'), types.KeyboardButton(text='5')]
        ],
        resize_keyboard=True
    )
    await message.answer('Как оцениваете чистоту заведения? \n(1 - Очень плохо, 2 - Плохо, 3 - Нормально,'
                         ' 4 - Хорошо, 5 - Отлично)', reply_markup=kb)


@review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    cleanliness_rating = message.text
    if cleanliness_rating not in ['1', '2', '3', '4', '5']:
        await message.answer('Пожалуйста, выберите рейтинг от 1 до 5')
        return
    await state.update_data(cleanliness_rating=cleanliness_rating)
    await state.set_state(RestourantReview.extra_comments)
    kb = types.ReplyKeyboardRemove()
    await message.answer('Дополнительный комментарий:', reply_markup=kb)


@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(extra_comments=extra_comments)
    data = await state.get_data()
    database.execute("""
        INSERT INTO review_results (name, instagram_username, visit_date, food_rating, cleanliness_rating, extra_comments)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data['name'], data['instagram_username'], data['visit_date'], data['food_rating'], data['cleanliness_rating'],
          data['extra_comments']))

    await state.clear()
    await message.answer("Спасибо за пройденный опрос")
