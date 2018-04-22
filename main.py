from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging as log
import random

updater = Updater(token='558762283:AAEMLDHAN2PkKyRQNVOHCBkVhkfXB4egOyU')
dispatcher = updater.dispatcher

dispatcher = updater.dispatcher


# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Бот на связи')


def textMessage(bot, update):
    personal_greetings(bot, update)
    response = '34 место получили Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


def randCommand(bot, update):
    response = 'Your number: ' + str(random.randint(1, 34))
    bot.send_message(chat_id=update.message.chat_id, text=response)


def helloCommand(bot, update):
    response = 'Hello ' + str(update.message.from_user.first_name) + ', I love ML'
    bot.send_message(chat_id=update.message.chat_id, text=response)

def personal_greetings (bot, update):
    response = 'Hello ' + str(update.message.from_user.first_name)
    bot.send_message(chat_id=update.message.chat_id, text=response)


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
rand_command_handler = CommandHandler('rand', randCommand)
hello_command_handler = CommandHandler('hello', helloCommand)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(rand_command_handler)
dispatcher.add_handler(hello_command_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
