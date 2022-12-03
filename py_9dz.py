# Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)

from telegram import Bot
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, ConversationHandler

bot = Bot(token='5840368801:AAF_Mj2uTITlBTMDXbhHSaf1XmNPYaKU50A')
updater = Updater(token='5840368801:AAF_Mj2uTITlBTMDXbhHSaf1XmNPYaKU50A')
dispahather = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет,\nвведи предложение ")

def correct(update, context):
    text = update.message.text.split()
    list = []
    for i in text:
        if 'абв' not in i:
            list.append(i)
    context.bot.send_message(update.effective_chat.id,' '.join(list))

# def weather(update, context):
#     text = update.message.text
#     if 'хор' in text.lower():
#         context.bot.send_message(update.effective_chat.id, "У меня тоже солнце")
#     else:
#         context.bot.send_message(update.effective_chat.id, "У природы нет плохой погоды")
#     return ConversationHandler.END

# def cancel(update, context):
#     context.bot.send_message(update.effective_chat.id, "Прощай!")

start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, correct)
# mes_weather_handler = MessageHandler(Filters.text, weather)
# mes_canc_handler = MessageHandler(Filters.text, cancel)

# conv_handler = ConversationHandler(entry_points=[start_handler],
#                                     states={A: [message_handler],
#                                             B: [mes_weather_handler]},
#                                     fallbacks= [mes_canc_handler])
dispahather.add_handler(start_handler)
dispahather.add_handler(message_handler)
# dispahather.add_handler(mes_canc_handler)

updater.start_polling()
updater.idle()