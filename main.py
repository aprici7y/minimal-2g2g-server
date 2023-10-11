import os
from tooGoodTooGo import TooGoodTooGo
from dotenv import load_dotenv
load_dotenv()



store_id = os.getenv('STORE_ID')
chat_id = os.getenv('CHAT_ID')
bot_token = os.getenv('BOT_TOKEN')


client = TooGoodTooGo(store_id, bot_token, chat_id) 

client.serve()

