
import telebot

bot = telebot.TeleBot('1869364233:AAEWyxbwOzhGI2vWe5HWhMrkavcyaQnvbcI')
with open("Preparat.txt", encoding="utf-8") as file:
    history = file.read()
with open("kak_prinimat.txt", encoding="utf-8" ) as file:
    kak_prinimat = file.read()

Protivopokazaniya = "El medicamento no tiene contraindicaciones. Es aceptada incluso por las madres lactantes "

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.reply_to(message, f'Hola, me llamo María y te ayudaré a perder peso. Es un placer conocerte  {message.from_user.first_name} ')

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Si')
    msg = bot.send_message(message.chat.id, text='¿Quiere saber más sobre el producto? ', reply_markup=keyboard)


@bot.message_handler(content_types = ['text'])
def step1(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row("Ver mi instagram🥰")
    keyboard.row("Obtener un enlace al producto👀")
    keyboard.row("Dígame, ¿cómo se toma estas gotas? ")
    keyboard.row("¿Hay alguna contraindicación?")
    keyboard.row("¿Cuál es la composición de las gotas?")
    keyboard.row("Ventajas de las gotas ?")
    keyboard.row("Los resulatados  de  algunos de mis suscriptores")

    if message.text == "Si":
        msg = bot.send_message(message.chat.id, text=history, reply_markup=keyboard)

    if message.text == "Ver mi instagram🥰":
        msg = bot.send_message(message.chat.id, text="https://www.instagram.com/mariabenitez_fit", reply_markup=keyboard)
    if message.text == "Obtener un enlace al producto👀":
        msg = bot.send_message(message.chat.id, text="https://linktr.ee/fitre", reply_markup=keyboard)
    if message.text == "Dígame, ¿cómo se toma estas gotas?":
        msg = bot.send_photo(message.chat.id,open('Kak_prinimat.jpg', 'rb'))
    if message.text == "¿Hay alguna contraindicación?":
        msg = bot.send_message(message.chat.id, text=Protivopokazaniya, reply_markup=keyboard)
    if message.text == "¿Cuál es la composición de las gotas?":
         msg = bot.send_photo(message.chat.id,open('sostav.jpg', 'rb'))
    if message.text == "Ventajas de las gotas ?":
        msg = bot.send_photo(message.chat.id, open('Preemushestva.jpg', 'rb'))
    if message.text == "Los resulatados  de  algunos de mis suscriptores":
        msg = bot.send_photo(message.chat.id, open('rezultat.jpg', 'rb'))
bot.polling(none_stop=True)