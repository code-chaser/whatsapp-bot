import json
from dotenv import load_dotenv
import os
import requests
import aiohttp
import asyncio
import constants

load_dotenv()
FACEBOOK_API_VERSION = os.getenv('FACEBOOK_API_VERSION')
WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN')
WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
WHATSAPP_RECIPIENT_ID = os.getenv('WHATSAPP_RECIPIENT_ID')

def send_whatsapp_test_message():
    url = f"{constants.FACEBOOK_API_BASE_URL}{FACEBOOK_API_VERSION}/{WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        'Authorization': f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        'Content-Type': 'application/json',
    }
    data = {
        "messaging_product": "whatsapp",
        "to": WHATSAPP_RECIPIENT_ID,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }
    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    response = send_whatsapp_test_message()
    print(response.json())
