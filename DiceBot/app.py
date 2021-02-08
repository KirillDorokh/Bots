import telebot
import random


TOKEN = '1526922305:AAGLALI2X3XHzUwYlJwAMJwiyV94i99aBIU'
bot = telebot.TeleBot(TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.add('1d4', '1d6', '1d8', '1d10', '1d12', '1d20', '2d20+', '2d20-', '1d100')


def random_dice(text):
    num = random.randint(1, int(text[2:]))
    return num


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    print(message)
    bot.send_message(message.chat.id, f'Ход', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_message(message):
    text = message.text
    if text[0] == '1':
        print(text)
        num = random_dice(text)
        print('num = ', num)
        bot.reply_to(message, num)
    elif text[0] == '2':
        num_1 = random.randint(1, 20)
        print('num_1 = ', num_1)
        num_2 = random.randint(1, 20)
        print('num_2 = ', num_2)
        if text[-1] == '+':
            highest = num_1 if num_1 > num_2 else num_2
            bot.reply_to(message, f'первый: {num_1}, второй: {num_2},'
                                  f'\nнаибольшее: {highest}')
        elif text[-1] == '-':
            lowest =  num_1 if num_1 < num_2 else num_2
            bot.reply_to(message, f'первый: {num_1}, второй: {num_2},'
                                  f'\nнаименьшее: {lowest}')



bot.polling(none_stop=True)