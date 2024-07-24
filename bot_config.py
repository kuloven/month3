from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from database.database import Database

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
group = getenv('GROUP_ID')
dp = Dispatcher()
database = Database('db_cafe.sqlite3')