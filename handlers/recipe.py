from aiogram import Router, types
from aiogram.filters.command import Command
from random import choice


recipe_router = Router()


@recipe_router.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    recipes = [
        'Рецепт 1: Пицца\nИнгредиенты: тесто, кетчуп, майонез, моцарелла, колбаса',
        'Рецепт 2: Борщ\nИнгредиенты: свекла, капуста, картошка, морковь, мясо',
        'Рецепт 3: Омлет\nИнгредиенты: яйца, молоко, соль, перец',
        'Рецепт 4: Гороховый суп\nИнгредиенты: горох, картошка, мясо',
        'Рецепт 5: Мясо по французски\nИнгредиенты: картошка, куринная голень, сыр любой, лук по желанию'
    ]
    random_recipe = choice(recipes)
    await message.reply(random_recipe)