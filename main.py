
import telebot

bot = telebot.TeleBot('1869364233:AAEWyxbwOzhGI2vWe5HWhMrkavcyaQnvbcI')
with open("History.txt", encoding="utf-8") as file:
    history = file.read()
f = open("KetoCookbook.pdf","rb")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.reply_to(message, f'Hello, my name is Maria, and I will help you lose weight. Pleased to meet you {message.from_user.first_name} ')

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Yes please, tell me about yourself and how do I lose weight? ')
    msg = bot.send_message(message.chat.id, text='Do you want to know a little bit about me?', reply_markup=keyboard)


@bot.message_handler(content_types = ['text'])
def step1(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('I want to learn more and get the recipe book')
    if message.text == "Yes please, tell me about yourself and how do I lose weight?":
        msg = bot.send_message(message.chat.id, text=history, reply_markup=keyboard)
        msg = bot.send_message(message.chat.id, text="To learn more and get your free recipe book, watch the video at the link below.", reply_markup=keyboard)
    if message.text == "I want to learn more and get the recipe book":
        msg = bot.send_message(message.chat.id, text="https://i-am.tel/bn4ge", reply_markup=keyboard)
        bot.send_document(message.chat.id, f)


bot.polling(none_stop=True)