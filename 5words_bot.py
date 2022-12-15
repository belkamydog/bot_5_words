import random
import telebot

N = 5

#
# @bot.message_handler(commands=['start'])
# def main(m):
#     bot.send_message(m.from_user.id, 'Добро пожаловать в Игру "5 букв"!!!')
#     bot.send_message(m.from_user.id, 'Нужно угадать слово из 5 букв.')
#     bot.send_message(m.from_user.id, 'Каждая попытка должна быть существительным в единственном числе.')
#     bot.send_message(m.from_user.id, 'Если буквы в этом слове нет, то на ее место втает *,')
#     bot.send_message(m.from_user.id, 'если есть, но на другом месте, то она становится строчной,')
#     bot.send_message(m.from_user.id, 'если есть и на правильном месте, то заглавной')
#     bot.send_message(m.from_user.id, 'Чтобы выйти из игры введите: exit')
#

rus_lib = open('russian_nouns.txt', 'r')
ru_list = [i.rstrip() for i in rus_lib if len(i.rstrip()) == N]
random_word = random.choice(ru_list)
rus_lib.close()
print(random_word)

rw, rl = random_word, ru_list
win = 0
bot = telebot.TeleBot('token')


@bot.message_handler(content_types=['text'])
def users(message):
    global win
    global rw
    global rl
    user_input = message.text
    if user_input == rw:
        win += 1
        output = f'Вы угадали!!!\nваш уровень: {win}\n*****'
        rw, rl = new_word()
        bot.send_message(message.from_user.id, output)
    elif user_input == 'exit':
        bot.send_message(message.from_user.id, 'До новых игр!!!')
    elif message.text == 'start':
        bot.send_message(message.from_user.id, 'Добро пожаловать в Игру "5 букв"!!!')
        bot.send_message(message.from_user.id, 'Нужно угадать слово из 5 букв.')
        bot.send_message(message.from_user.id, 'Каждая попытка должна быть существительным в единственном числе.')
        bot.send_message(message.from_user.id, 'Если буквы в этом слове нет, то на ее место втает *,')
        bot.send_message(message.from_user.id, 'если есть, но на другом месте, то она становится строчной,')
        bot.send_message(message.from_user.id, 'если есть и на правильном месте, то заглавной')
        bot.send_message(message.from_user.id, 'Чтобы выйти из игры введите: exit')
    else:
        w = game(user_input, rw, rl)
        bot.send_message(message.from_user.id, w)


def new_word():
    rus_lib = open('rus_lib.txt', 'r')
    ru_list = [i.rstrip() for i in rus_lib if len(i.rstrip()) == N]
    random_word = random.choice(ru_list)
    rus_lib.close()
    print(random_word)
    return random_word, ru_list


def game(user_input, r_word, ru_l):
    if len(user_input) == N:
        answer = []
        for i in range(N):
            if user_input[i] == r_word[i]:
                answer.append(user_input[i].upper())
            elif user_input[i] in r_word and user_input[i] != r_word[i]:
                answer.append(user_input[i].lower())
            else:
                answer.append('*')
        return ' '.join(answer)
    else:
        output = f'Введите существительное из {N} букв!'
        return output


bot.polling(none_stop=True, interval=0)
#add new library
