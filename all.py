from click import command
import birthday as brth
import kabachks as kab
import telebot
import threading as th
import datetime as dt

with open("bot_token.txt", "r") as f:
  bot_token = f.read()

bot = telebot.TeleBot(bot_token)
is_working = False
timer_pingall = True
congratulations_started = False

# Processing "/start" and "/end" commands to start and end the bot's job respectively
@bot.message_handler(commands=['start', 'end'])
def send_message(message):
  global is_working
  global congratulations_started
  if message.text == '/start' or message.text == '/start@Cmokchybot':
    is_working = True
    sent_message = bot.send_message(message.chat.id, "Починаю свою роботу")
    with open("id.txt", "w") as f:
      f.write(str(message.chat.id))
    
    if not congratulations_started:
      with open("id.txt", "r") as f:
        congratulations_started = True
        brth.congratulations(f.read(), bot)

  if message.text == '/end' or message.text == '/end@Cmokchybot':
    is_working = False
    bot.send_message(message.chat.id, "Завершую свою роботу")

# A function, that processes a "/pingall" command to send a message,
# that notifies all group members
@bot.message_handler(commands=['pingall'])
def send_message(message):
  global timer_pingall
  if is_working:
    if timer_pingall:
      bot.send_message(message.chat.id, kab.inline_notify_add("КАБАЧКИ "), "MarkdownV2")
      timer_pingall = False
      th.Timer(60, reset_timer_pingall).start()
    else:
      bot.send_message(message.chat.id, "Пінг на таймауті")

# Resets the timer for "/pingall" command
def reset_timer_pingall():
  global timer_pingall
  timer_pingall = True

bot.infinity_polling()