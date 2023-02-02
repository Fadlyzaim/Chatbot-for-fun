import telebot
import datetime

bot = telebot.TeleBot("6171619900:AAG24gBjA5VPbR2axxvabCA71ZQ72MSonlQ")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I am a chatbot. How can I help you today?")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, "Hello! How are you doing today?")
    elif message.text.lower() == 'time':
        bot.send_message(message.chat.id, "The current time is: " + str(datetime.datetime.now().time()))
    elif message.text.lower() == 'date':
        bot.send_message(message.chat.id, "The current date is: " + str(datetime.datetime.now().date()))
    else:
        bot.send_message(message.chat.id, "I am sorry, I do not understand your question.")

bot.polling()


