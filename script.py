import threading
from TeleBot import TeleBot
import telebot


bot = TeleBot()
bot.start()
bot.send_message(markup=bot.markup_builder("button1", "button2", "/kill"))
