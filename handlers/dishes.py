from aiogram import Router, F, types


dishes_router = Router()


@dishes_router.message(F.text =='Холодный напиток')
async def dishes_handler(message: types.Message):
    photo = types.FSInputFile('images_2/cola.jpg')
    await message.answer_photo(
        photo=photo,
        caption="Холодный напиток")


@dishes_router.message(F.text == 'Блюдо')
async def disnes_handler(message: types.Message):
    photo2 = types.FSInputFile('images_2/hincali.jpg')
    await message.answer_photo(
        photo=photo2,
        caption='Блюдо Хинкали')