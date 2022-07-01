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

# Condition to check, whether it is a leap year
def is_leap_year():
  return not (dt.datetime.now().year % 4)

# A function, that returns a time to certain month and day of this year in seconds
def countdown_to_function(needed_datetime):
  birth_day_and_month = dt.datetime(dt.datetime.now().year,
                                      needed_datetime.month,
                                      needed_datetime.day)
  return (birth_day_and_month - dt.datetime.now()).total_seconds()

# A function, that delays current countdown for certain time in days
def delay_countdown_days(countdown_now, time_in_days):
  return countdown_now + dt.timedelta(days=time_in_days).total_seconds()

# A function, that delays current countdown for certain time in hours
def delay_countdown_hours(countdown_now, time_in_hours):
  return countdown_now + dt.timedelta(hours=time_in_hours).total_seconds()

# Send the scheduled congratulation message to the group
def congratulations(message_chat_id):
  for kabachk in kab.kabachks.values():
    time_to_run = countdown_to_function(kabachk)
    time_to_run = delay_countdown_hours(time_to_run, 10) # The function will execute at 10:00 AM
    if time_to_run < 0:
      time_to_run = delay_countdown_days(time_to_run, 365) # If the countdown is negative(this date has passed in this year), the function will execute in the next year
    if is_leap_year():
      time_to_run = delay_countdown_days(time_to_run, 1) # If this year is leap, add one day to the countdown
    
    th.Timer( time_to_run,
              brth.congratulate_kabachk,
              [kabachk, message_chat_id]).start()

with open("bot_token.txt", "r") as f:
  congratulations(f.read())

bot.infinity_polling()