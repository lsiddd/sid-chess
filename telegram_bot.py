import logging
import telegram
from telegram.error import NetworkError, Unauthorized

class TelegramBot:

    # check if GO has been notified
    notified_game_over = False

    def __init__ (self, token):
        self.bot =  telegram.Bot(token)
        try:
            self.update_id = self.bot.get_updates()[0].update_id
        except IndexError:
            self.update_id = None
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.chat_id = self.bot.get_updates(timeout=10)[-1].message.chat_id


    def send_message(self, text):
        self.bot.send_message(self.chat_id, text)
        

    def send_board(self):
        self.bot.send_photo(chat_id=self.chat_id, photo=open(f'boards/{self.chat_id}.png', 'rb'))
        # return bot

    def listen_for_command(self):
        # Request updates after the last update_id
        for update in self.bot.get_updates(offset=self.update_id, timeout=10):
            self.update_id = update.update_id + 1
            if update.message:  # your bot can receive updates without messages
                user_move  = update.message.text
                if (type(user_move) != 'NoneType'):
                    return user_move
                else:
                    # for to return a string if no message
                    return ""


    def get_user_move(self):
        """get the user move from the messave received
        """
        while (True):
            try:
                # Request updates after the last update_id
                for update in self.bot.get_updates(offset=self.update_id, timeout=10):
                    self.update_id = update.update_id + 1
                    if update.message:  # your bot can receive updates without messages
                        user_move  = update.message.text
                        # update.message.reply_text(out)
                        if (type(user_move) != 'NoneType'):
                            return user_move
            except:
                pass