import asyncio
import os
from datetime import date

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Получаем токен из переменных окружения Render
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Токен не найден! Добавь переменную TOKEN в Environment Variables на Render")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

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
    years = days / 365.0
    human_age = cat_to_human_years(years)

    await message.reply(
        f"Мия\n"
        f"{days} дней (~{years:.2f} лет)\n"
        f"~{human_age} человеческих лет"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
