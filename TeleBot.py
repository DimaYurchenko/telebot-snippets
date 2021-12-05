import telebot
from threading import Thread
from dotenv import load_dotenv
import os
from collections.abc import Sequence


class TeleBot(Thread):

    def __init__(self, token: str = None, id: int = None):
        """
        Args:
            token (str, optional): Your bot's token. Default value is loaded from .env.
            id (int, optional): Id of user you want to send messages to. Default value is loaded from .env.
        """
        load_dotenv()

        if token is None:
            self.TOKEN = os.environ.get("TOKEN")
        else:
            self.TOKEN = token

        if id is None:
            self.account_id = int(os.environ.get("id"))
        else:
            self.account_id = id

        self.bot = telebot.TeleBot(self.TOKEN, parse_mode=None)

        Thread.__init__(self)

    def run(self) -> None:

        bot = self.bot

        @bot.message_handler(commands=["kill"])
        def stop_script(message):
            self.send_message("killed")

        bot.polling(none_stop=True)  # set interval later

    def markup_builder(self, *args: str):
        markup = telebot.types.ReplyKeyboardMarkup()
        for value in args:
            markup.add(value)

        return markup

    def send_message(self, message: str = "testing 🤖", id: int = None, markup=None):
        if id is None:
            id = self.account_id

        self.bot.send_message(id, message, reply_markup=markup)

    def log_error(self, error: str = "something went wrong 😥", id: int = None):
        if id is None:
            id = self.account_id

        self.send_message(error, id)


# getInput options
