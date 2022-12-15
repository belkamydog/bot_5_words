import telebot
import game_5_words

bot = telebot.TeleBot('5908717917:AAEsZzQ_rGrwzImO0p3UEO1-6Qqi7xNkpmg')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message.text


bot.polling(none_stop=True, interval=0)
