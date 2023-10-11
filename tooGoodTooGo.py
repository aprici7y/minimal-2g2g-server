import random
import time
from tgtg import TgtgClient
import telebot
import logging
from datetime import datetime, timedelta





class TooGoodTooGo:

    def __init__(self, favorite_store, token, chat_id):
        self.client = TgtgClient(email="karaffen-panini0i@icloud.com")
        self.client.get_credentials()
        self.store_id = favorite_store
        self.chat_id = chat_id
        self.bot = telebot.TeleBot(token, parse_mode=None)




    def test_tele(self):
        print(self.chat_id)
        self.bot.send_message(self.chat_id, 'deployed')


    def is_evening(self):
        ## system time stuff, add your own time diff to universal time
        now = datetime.now() + timedelta(hours=3)
        today_6_pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
        print(today_6_pm)
        if(now > today_6_pm):
            return True
        return False

    def poll_loop(self):
        logging.info('server seems to be healthy')
        random_time_range = random.randint(45, 120)
        time.sleep(random_time_range)
        item = self.client.get_item(item_id=self.store_id)
        logging.info(item['items_available'])
        if(item['items_available'] > 0):
            self.bot.send_message(self.chat_id, 'avaible')
        logging.info('keeping running')

    def serve(self):
        self.bot.send_message(self.chat_id, 'deployed')
        while(True):
            if (self.is_evening()):
                self.poll_loop()