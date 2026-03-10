import os
import telebot

# Obtener el token 
BOT_TOKEN = os.environ.get('BOT_TOKEN') 
bot = telebot.TeleBot(BOT_TOKEN) 

# Responder a los comandos /start o /hola 
@bot.message_handler(commands=['start', 'hola']) 
def enviar_bienvenida(mensaje):
    bot.reply_to(mensaje, "Hola, ¿como estás?") 

# Repetir cualquier otro mensaje 
@bot.message_handler(func=lambda msg: True) 
def enviar_echo(mensaje):
    bot.reply_to(mensaje, mensaje.text) 

# Iniciar la escucha de mensajes 
bot.infinity_polling()