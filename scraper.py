import requests
from bs4 import BeautifulSoup 
import logging
from dotenv import dotenv_values
import asyncio
import telegramHelper

ENV = dotenv_values('.env')

URL = ENV['SITE_URL']


async def index():
    print('Running')

    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    noneAvailableElement = soup.find('em', string="We don't have any garages available right now, please check back another time")
    noneAvailable = bool(noneAvailableElement)

    print(noneAvailable)

    if noneAvailable == True: 
        message = 'None available'
    else:
        message = 'AVAILABLE'

    await telegramHelper.sendMessage(message)

asyncio.run(index())