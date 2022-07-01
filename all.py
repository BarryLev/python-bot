from click import command
import birthday as brth
import kabachks as kab
import telebot
import threading as th
import datetime as dt
import os

with open("bot_token.txt", "r") as f:
  bot_token = f.read()

print(bot_token)

bot = telebot.TeleBot(bot_token)
is_working = False
timer_pingall = True

@bot.message_handler(commands=['start', 'end'])
def send_message(message):
  global is_working
  if message.text == '/start':
    is_working = True
    bot.send_message(message.chat.id, "Починаю свою роботу")
    # with open("id.txt", "w") as f:
    #   f.write(str(message.from_user.id))

  if message.text == '/end':
    is_working = False
    bot.send_message(message.chat.id, "Завершую свою роботу")

@bot.message_handler(commands=['pingall'])
def send_message(message):
  global timer_pingall
  if is_working and timer_pingall:
    bot.send_message(message.chat.id,  "КАБАЧКИ!!! \n" + kab.get_kabachks())
    timer_pingall = False
    th.Timer(60, reset_timer_pingall).start()

def reset_timer_pingall():
  global timer_pingall
  timer_pingall = True

def congratulations():
  for key in kab.kabachks:
    birth_day_and_month = dt.datetime(dt.datetime.now().year,
                                      kab.kabachks[key][1].month,
                                      kab.kabachks[key][1].day,
                                      10)
    time_to_run = (birth_day_and_month - dt.datetime.now()).total_seconds()
    if time_to_run < 0:
      time_to_run = time_to_run + dt.timedelta(days=365).total_seconds()
    if dt.datetime.now().year % 4 == 0:
      time_to_run = time_to_run + dt.timedelta(days=1).total_seconds()
    th.Timer( time_to_run,
              brth.congratulate_kabachk,
              [kab.kabachks[key]]).start()

congratulations()

bot.infinity_polling()