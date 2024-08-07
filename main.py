import telebot

bot = telebot.TeleBot('7292799374:AAFQkJy_XvW3-DlYPyBhxhhnS7NUBOaf0pA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет', parse_mode='Markdown')


@bot.message_handler(commands=['varvideo'])
def main(message):
    bot.send_message(message.chat.id, '[Основы переменных](https://youtu.be/uZKX9hGQiSw)', parse_mode='Markdown')


@bot.message_handler(commands=['stringvideo'])
def main(message):
    bot.send_message(message.chat.id, '[Основы строк](https://youtu.be/ONvctQXUWHc)', parse_mode='Markdown')


@bot.message_handler(commands=['functionsvideo'])
def main(message):
    bot.send_message(message.chat.id, '[Функции](https://youtu.be/GOhfHzO1_z0)', parse_mode='Markdown')


bot.infinity_polling()
