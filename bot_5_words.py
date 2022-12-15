import telebot
import game_5_words

bot = telebot.TeleBot('token')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message.text


bot.polling(none_stop=True, interval=0)
