from click import command
import birthday as brth
import kabachks as kab
import telebot
import threading as th
import datetime as dt
import pprint as pp

with open("bot_token.txt", "r") as f:
  bot_token = f.read()

with open("my_id.txt", "r") as f:
  my_id = f.read()

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
  print(message.from_user.id)
  if is_working:
    if timer_pingall or message.from_user.id == my_id:
      bot.send_message(message.chat.id, kab.inline_notify_add("КАБАЧКИ\n", True), "MarkdownV2")
      timer_pingall = False
      th.Timer(60, reset_timer_pingall).start()
    else:
      bot.send_message(message.chat.id, "Пінг на таймауті")

@bot.message_handler(commands=['when'])
def send_message(message):
  if is_working:
    splitted_command = message.text.split()
    if len(splitted_command) == 2:
      brth.get_time_to_next_birthday(splitted_command[1], message.chat.id, bot)
    elif len(splitted_command) == 1:
      try:
        markup = kab.send_list_of_kabacks()
        msg = bot.send_message(message.chat.id, "Вибери людину, чий день народження ти хочеш дізнатись", reply_markup=markup)
        pp.pprint(str(markup.to_json()))
        bot.register_next_step_handler(msg, brth.send_text_from_message, message.chat.id, bot)
      except Exception as e:
        bot.send_message(message.chat.id, "Під час обробки імені сталась помилка, повідомлення було написано вручну")
    else:
      bot.send_message(message.chat.id, "Введена неправильна кількість аргументів")

# Resets the timer for "/pingall" command
def reset_timer_pingall():
  global timer_pingall
  timer_pingall = True

@bot.message_handler(commands=['test'])
def send_message(message):
  bot.send_message(message.chat.id, "Тест [Slendi505](tg://user?id=511396241) [slavonch](tg://user?id=618621657)", "MarkdownV2")

bot.infinity_polling()