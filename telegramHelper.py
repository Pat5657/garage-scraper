from dotenv import dotenv_values
from telegram import Bot

ENV = dotenv_values('.env')

ACCESS_TOKEN = ENV['TELEGRAM_BOT_ACCESS_TOKEN']
CHANNEL_ID = ENV['TELEGRAM_CHANNEL_ID']

bot = Bot(ACCESS_TOKEN)

async def sendMessage(message: str):
    return await bot.send_message(
        chat_id=CHANNEL_ID,
        text=message
    )