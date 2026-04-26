import asyncio
import os
from datetime import date

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command  # ← добавили это

# Получаем токен из переменных окружения на Render
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Токен не найден! Убедись, что в Environment Variables есть переменная TOKEN")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

birth_date = date(2025, 1, 30)

def cat_to_human_years(cat_age: float) -> int:
    if cat_age < 1:
        return int(cat_age * 15)
    elif cat_age <= 2:
        return 15 if cat_age == 1 else 24
    else:
        return 24 + (int(cat_age) - 2) * 4

@dp.message(Command("start"))          # ← исправлено
async def start(message: types.Message):
    today = date.today()
    days = (today - birth_date).days
    years = days / 365.0
    human_age = cat_to_human_years(years)

    await message.reply(
        f"🐱 <b>Мия</b>\n\n"
        f"Возраст: {days} дней\n"
        f"(~{years:.2f} лет)\n"
        f"≈ {human_age} человеческих лет",
        parse_mode=ParseMode.HTML
    )

# Реакция на любые другие сообщения
@dp.message()                          # ← исправлено
async def echo(message: types.Message):
    if message.text and not message.text.startswith('/'):
        await message.answer("Я пока понимаю только команду /start 😊")

async def main():
    print("Бот успешно запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
