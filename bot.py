import telegram
from telegram.ext import Updater, CommandHandler, Handler
import datetime 
from conf.settings import TELEGRAM_TOKEN


class Bot:
    def __init__(self):
        self.d2 = datetime.datetime.strptime('2020-08-21', '%Y-%m-%d')
        self.d1 = datetime.datetime.now()

        self.msg = "Fala😎!\n"
        self.msg += "Me pergunta e eu te digo quanto tempo falta pro Caiochella!.\n"
        self.msg += "Pra isso é só digitar /quanto. \n"
        self.msg += "Afinal, tu não vai perder, né?!😉\n"


    def start(self, bot, update):
        me = bot.get_me()
        bot.send_message(chat_id=update.message.chat_id,
                        text=self.msg,
                        reply_markup=reply_kb_markup)

    def calculateDate(self):
        if self.d1>self.d2:
            return "Desculpa, mas o aniversário já passou!"
        else:
            return 'faltam só '+ str(abs((self.d2 - self.d1).days)) + ' dias pro rock doido 😎!'
    
    def data(self, bot, update):
        msg = self.calculateDate()
        bot.send_message(chat_id=update.message.chat_id, text= msg)

bot = Bot()
updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher
updater.start_polling()

start_handler = CommandHandler('start', bot.start)
dispatcher.add_handler(start_handler)
data_handler = CommandHandler('quanto', bot.data)
dispatcher.add_handler(data_handler)
