import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "SIZNING_BOT_TOKEN"
bot = Bot("7967482218:AAEb0GbRx7qfaktaAYEAmkQxM18_iOQoKYs"(
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Salom! Bot ishga tushdi!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
