import asyncio
import logging
from aiogram import Bot
from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.my_info import my_info_router
from handlers.recipe import recipe_router
from handlers.echo import echo_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router
from handlers.menu import menu_router
from handlers.group import group_router

async def on_startup(bot: Bot):
    database.create_tables()

async def main():
    # запуск бота
    dp.include_router(start_router)
    dp.include_router(review_router)
    dp.include_router(my_info_router)
    dp.include_router(recipe_router)
    dp.include_router(dishes_router)
    dp.include_router(menu_router)
    dp.include_router(group_router)
    # В конце
    dp.include_router(echo_router)
    # При запуске
    dp.startup.register(on_startup)
    #  Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())