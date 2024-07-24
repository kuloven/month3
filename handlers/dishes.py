from aiogram import Router, F, types
from AllHomework import database

dishes_router = Router()


@dishes_router.message(F.text =='Кола')
async def dishes_handler(message: types.Message):
    photo = types.FSInputFile('images_2/cola.jpg')
    await message.answer_photo(
        photo=photo,
        caption="Холодный кола")

@dishes_router.message(F.text == 'Хинкали')
async def dishes_handler(message: types.Message):
    photo2 = types.FSInputFile('images_2/hincali.jpg')
    await message.answer_photo(
        photo=photo2,
        caption='Хинкали')

@dishes_router.message(F.text == 'Блинчики')
async def dishes_handler(message: types.Message):
    photo4 = types.FSInputFile('images_2/blinchiki.jpg')
    await message.answer_photo(
        photo=photo4,
        caption='Блинчики')