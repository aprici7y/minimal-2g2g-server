import logging
import os
from tooGoodTooGo import TooGoodTooGo
from dotenv import load_dotenv
load_dotenv()







def main():
    logging.basicConfig(level=logging.INFO)
    store_id = os.getenv('STORE_ID')
    chat_id = os.getenv('CHAT_ID')
    bot_token = os.getenv('BOT_TOKEN')

    wrapper = TooGoodTooGo(store_id, bot_token, chat_id) 
    wrapper.serve()


if __name__ == '__main__':
    main()

