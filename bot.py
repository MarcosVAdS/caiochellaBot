import telegram
import configparser
import redis
from telegram.ext import Updater, CommandHandler, Handler
import datetime 
from conf.settings import TELEGRAM_TOKEN
#import pandas as pd

class Bot:
    def __init__(self):
        self.d2 = datetime.datetime.strptime('2020-08-21', '%Y-%m-%d')
        self.d1 = datetime.datetime.now()

        self.msg = "Fala manx 😎!\n"
        self.msg += "Me pergunta e eu te digo quanto tempo falta pro Caiochella!.\n"
        self.msg += "Pra isso é só digitar /quanto. \n"
        self.msg += "Afinal, tu não és leso de perder, né?!😉\n"


    def start(self, bot, update):
        me = bot.get_me()
        #main_menu_keyboard = [[telegram.KeyboardButton('/quanto')]]

        #reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
        #                                            resize_keyboard=True,
        #                                            one_time_keyboard=True)

        bot.send_message(chat_id=update.message.chat_id,
                        text=self.msg,
                        reply_markup=reply_kb_markup)

    def calculateDate(self):
        print(self.d1)
        print(self.d2)
        #print(abs(self.d2 - self.d1).days)
        return abs((self.d2 - self.d1).days)
    
    def data(self, bot, update):
        data = str(self.calculateDate())
        bot.send_message(chat_id=update.message.chat_id, text= 'faltam só ' + data + ' dias' + ' pro rock doido 😎!')


#db = redis.StrictRedis(host=config['DB']['host'],
#                       port=config['DB']['port'],
#                       db=config['DB']['db'])

bot = Bot()
updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher
updater.start_polling()

start_handler = CommandHandler('start', bot.start)
dispatcher.add_handler(start_handler)
data_handler = CommandHandler('quanto', bot.data)
dispatcher.add_handler(data_handler)
