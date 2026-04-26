from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from datetime import date
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

birth_date = date(2025, 1, 30)

def cat_to_human_years(cat_age):
    if cat_age < 1:
        return int(cat_age * 15)
    elif cat_age == 1:
        return 15
    elif cat_age == 2:
        return 24
    else:
        return 24 + (cat_age - 2) * 4

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    today = date.today()
    days = (today - birth_date).days
    years = days / 365
    human_age = cat_to_human_years(years)

    await message.reply(
        f"🐱 Мия\n"
        f"📅 {days} дней (~{years:.2f} лет)\n"
        f"👨 ~{human_age} человеческих лет"
    )

if __name__ == "__main__":
    executor.start_polling(dp)
