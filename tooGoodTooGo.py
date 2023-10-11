import random
import time
from tgtg import TgtgClient
import telebot





class TooGoodTooGo:

    def __init__(self, favorite_store, token, chat_id):
        self.client = TgtgClient(email="karaffen-panini0i@icloud.com")
        self.store_id = favorite_store
        self.chat_id = chat_id
        self.bot = telebot.TeleBot(token, parse_mode=None)




    def test_tele(self):
        print(self.chat_id)
        self.bot.send_message(self.chat_id, 'deployed')



    def serve(self):
        self.bot.send_message(self.chat_id, 'deployed')
        while(True):
            random_time_range = random.randint(45, 120)
            time.sleep(random_time_range)
            item = self.client.get_item(item_id=self.store_id)
            if(item['items_available'] > 0):
                self.bot.send_message(self.chat_id, 'avaible')

                

