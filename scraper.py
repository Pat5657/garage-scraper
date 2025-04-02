import requests
from bs4 import BeautifulSoup 
import logging
from dotenv import dotenv_values
import asyncio
import telegramHelper

ENV = dotenv_values('.env')

logging.basicConfig(
    filename='script.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


URL = ENV['SITE_URL']


async def index():
    print('Running')
    logging.info('Running')

    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    noneAvailableElement = soup.find('em', string="We don't have any garages available right now, please check back another time")
    noneAvailable = bool(noneAvailableElement)

    print(noneAvailable)

    if noneAvailable == True: 
        message = 'None available'
    else:
        message = 'AVAILABLE'

    logging.info('Availability: ' + message)

    await telegramHelper.sendMessage(message)

asyncio.run(index())