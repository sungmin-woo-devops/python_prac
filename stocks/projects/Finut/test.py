import telegram
import asyncio

# Telegram Bot API Token 설정
token = "6211772659:AAH4EkVm6vcoWYAmiZ6y2UUutQ0Pu9ZVpKA"
chat_id = "5585664885"
bot = telegram.Bot(token=token)

# bot.sendMessage(chat_id=chat_id, text="Hello World!")

async def send_telegram_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)
    
asyncio.run(send_telegram_message(chat_id=chat_id, text="Hello, Telegram Bot!"))

# async def get_updates():
#     updates = await bot.get_updates()
#     return updates

# asyncio.run(get_updates())

# # Telegram Chat ID 설정
# chat_id = ""

# # 전송할 메시지 설정
# message = ""

# # Telegram API URL 설정
# URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, CHAT_ID, MESSAGE)

# # Telegram 메시지 전송
# response = requests.get(URL)
# print(response.json())