import birthday as brth
import kabachks as kab
import telebot
import threading as th

with open("bot_token.txt", "r") as f:
  bot_token = f.read()

with open("my_id.txt", "r") as f:
  my_id = f.read()

bot_name = "@Cmokchybot"
bot = telebot.TeleBot(bot_token)
is_working = False
timer_pingall = True
congratulations_started = False

# Returns "True", when the command was called with the short type, or with the bot name
def is_command_called(this_command, command):
  return this_command == command or this_command == command + bot_name

# Processing "/start" and "/end" commands to start and end the bot's job respectively
@bot.message_handler(commands=['start', 'end'])
def send_message(message):
  global is_working
  global congratulations_started
  if is_command_called(message.text, '/start'):
    is_working = True
    bot.send_message(message.chat.id, "Починаю свою роботу")
    
    if not congratulations_started:
      congratulations_started = True
      brth.congratulations(message.chat.id, bot)

  if is_command_called(message.text, '/end'):
    is_working = False
    bot.send_message(message.chat.id, "Завершую свою роботу")

# A function, that processes a "/pingall" command to send a message,
# that notifies all group members
@bot.message_handler(commands=['pingall'])
def send_message(message):
  global timer_pingall
  if is_working:
    if timer_pingall or message.from_user.id == my_id:
      bot.send_message(message.chat.id, kab.inline_notify_add("КАБАЧКИ\n", True), "MarkdownV2")
      timer_pingall = False
      th.Timer(60, reset_timer_pingall).start()
    else:
      bot.send_message(message.chat.id, "Пінг на таймауті")

# A function, that processes a "/when" command to send a message,
# that shows time to birthday
@bot.message_handler(commands=['when'])
def send_message(message):
  if is_working:
    splitted_command = message.text.split()
    if len(splitted_command) == 2:
      brth.send_time_to_next_birthday(splitted_command[1], message.chat.id, bot)
    elif len(splitted_command) == 1:
      try:
        markup = kab.send_list_of_kabacks_to_keyboard()
        sent_message = "[{tag}](tg://user?id={id})".format(tag = "Гей", id = message.from_user.id)
        sent_message = sent_message + ", вибери людину, чий день народження ти хочеш дізнатись"
        msg = bot.send_message(message.chat.id, sent_message, parse_mode="MarkdownV2", reply_markup=markup)
        bot.register_next_step_handler(msg, brth.send_text_from_message, message.chat.id, bot)
      except Exception as e:
        bot.send_message(message.chat.id, "Під час обробки імені сталась помилка, можливо повідомлення було написано вручну")
        print(e)
    else:
      bot.send_message(message.chat.id, "Введена неправильна кількість аргументів")

# Resets the timer for "/pingall" command
def reset_timer_pingall():
  global timer_pingall
  timer_pingall = True

bot.infinity_polling()