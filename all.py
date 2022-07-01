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

# Processing "/start" and "/end" commands to start and end the bot's job respectively
@bot.message_handler(commands=['start', 'end'])
def send_message(message):
  global is_working
  if message.text == '/start':
    is_working = True
    bot.send_message(message.chat.id, "Починаю свою роботу")
    with open("id.txt", "w") as f:
      f.write(str(message.chat.id))

  if message.text == '/end':
    is_working = False
    bot.send_message(message.chat.id, "Завершую свою роботу")

# A function, that processes a "/pingall" command to send a message,
# that notifies all group members
@bot.message_handler(commands=['pingall'])
def send_message(message):
  global timer_pingall
  if is_working and timer_pingall:
    bot.send_message(message.chat.id,  "КАБАЧКИ!!! \n" + kab.get_kabachks())
    timer_pingall = False
    th.Timer(60, reset_timer_pingall).start()

# Resets the timer for "/pingall" command
def reset_timer_pingall():
  global timer_pingall
  timer_pingall = True

# Send the scheduled congratulation message to the group
def congratulations(message_chat_id):
  for kabachk in kab.kabachks.values():
    

with open("bot_token.txt", "r") as f:
  congratulations(f.read())

bot.infinity_polling()