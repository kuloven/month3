import re

from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


review_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@review_router.message(Command('feedback'))
async def start_review(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await message.answer('Как вас зовут?')


@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    if not name.isalpha():
        await message.answer('Вводите только буквы')
        return
    print(message.text)
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.instagram_username)
    await message.answer('Ваш инстаграмм профиль? ')


@review_router.message(RestourantReview.instagram_username)
async def process_instagram_username(message: types.Message, state: FSMContext):
    print(message.text)
    await state.update_data(instagram_username=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Пожалуйста, введите дату вашего посещения (только цифры):")

@review_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    visit_date = message.text
    if re.match(r'^\d{2}\.\d{2}\.\d{2}$', visit_date):
        if not visit_date.isdigit():
            await message.answer('Введите только цифры ДД.ММ.ГГ')
        return
    await state.set_state(RestourantReview.food_rating)
    await state.update_data(visit_date=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Хорошо'),
                types.KeyboardButton(text='Плохо'),
                types.KeyboardButton(text='Нормально')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Как оцениваете качество еды?', reply_markup=kb)

@review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.cleanliness_rating)
    await state.update_data(food_rating=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Чисто'),
                types.KeyboardButton(text='Грязно'),
                types.KeyboardButton(text='Пыльно'),
                types.KeyboardButton(text='Нормально')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Как оценивается чистоту заведения?', reply_markup=kb)
    await RestourantReview.cleanliness_rating.set()


@review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestourantReview.extra_comments)
    kb = types.ReplyKeyboardRemove()
    await message.answer('Оставьте свой отзыв: ', reply_markup=kb)

@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message:  types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(comments=extra_comments)
    data = await state.get_data()
    print(data)
    await state.clear()

    await message.answer("Спасибо за пройденный опрос")

