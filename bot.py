import telebot

# استبدل 'YOUR_API_TOKEN' بالتوكن الذي حصلت عليه من BotFather
API_TOKEN = '7510110263:AAEZsWVdMJZFm1ZCeGyG6CYI0xfIeqytiLQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "مرحبا")

bot.polling()
