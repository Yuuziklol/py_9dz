# Создайте Бота для игры с конфетами человек против бота. (Дополнительно)
from random import randint
from telegram import Bot
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, ConversationHandler

bot = Bot(token='5840368801:AAF_Mj2uTITlBTMDXbhHSaf1XmNPYaKU50A')
updater = Updater(token='5840368801:AAF_Mj2uTITlBTMDXbhHSaf1XmNPYaKU50A')
dispahather = updater.dispatcher

player_move = 0
bot_move = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет, сегодня мы сыграем в игру с конфетами.\nКаждый игрой может взять от 1 до 28 конфет.\nПервый ход определяется жеребьевкой.\nИгрок, забравший последние конфеты, выигрывает!")

def player(update, context,count,number):
    if number == 1 and count != 0:
        return bot_move
    player_candies = int(update.message.text)
    count -= player_candies
    context.bot.send_message(update.effective_chat.id, f"Осталось {count} конфет")
    if count == 0:
        context.bot.send_message(update.effective_chat.id, f"Поздравляем, вы победили")
        return ConversationHandler.END
    else:
        number == 1
        return bot_move

def game_bot(update, context,count,max_win_pos,cycle,number):
    if number == 0 and count != 0:
        return bot_move
    if count != max_win_pos - (29 * cycle):
        help = count
        count = (max_win_pos - (29 * (cycle)))
        context.bot.send_message(update.effective_chat.id, f"Я взял {help-count} конфет, осталось {count} конфет")
    else:
        help = count
        count -= randint(1,28)
        context.bot.send_message(update.effective_chat.id, f"Я взял {help-count} конфет, осталось {count} конфет")
    cycle += 1
    if count == 0:
        context.bot.send_message(update.effective_chat.id, f"Ха-ха, я победил, попробуй еще раз")
        return ConversationHandler.END
    else:
        number == 0
        return player_move
    

def cancel(update, context,number):
    context.bot.send_message(update.effective_chat.id, f"Игра завершена, победил {number} игрок")

number = randint(0,1)
count = 2021
cycle = 0
max_win_pos = 29 * (count // 29)
update= ''
context= ''
start_handler = CommandHandler("start", start)
bot_handler = CommandHandler(Filters.text, game_bot(update,context,count,max_win_pos,cycle,number))
player_handler = CommandHandler(Filters.text, player(update,context,count,number))
mes_canc_handler = CommandHandler(Filters.text, cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={player_move: [player],
                                            bot_move: [game_bot]},
                                    fallbacks= [mes_canc_handler])

dispahather.add_handler(conv_handler)

updater.start_polling()
updater.idle()






