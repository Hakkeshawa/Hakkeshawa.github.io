import requests
from main import get_weather
from config import tg_token, weather_token
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

bot = Bot(token=tg_token)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def start_com(message: Message):
    await message.answer("Привет! Напиши название города и я отправлю сводку погоды")

@dp.message()
async def weather_command(message: Message):
    city = message.text
    try:
        reply = get_weather(city, weather_token)
        await message.answer(reply)
    except Exception as e:
        await message.answer("Проверьте имя города")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
