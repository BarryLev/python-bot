import datetime as dt
from telebot import types
import kabachks as kab
import asyncio

# Checks whether this datetime has passed
def is_datetime_passed(this_datetime, additional_hours):
  if dt.datetime.now().month > this_datetime.month:
    return True
  if dt.datetime.now().month == this_datetime.month and dt.datetime.now().day > this_datetime.day:
    return True
  if dt.datetime.now().month == this_datetime.month and dt.datetime.now().day == this_datetime.day and dt.datetime.now().hour > additional_hours:
    return True
  return False

# A function, that returns a time to certain month and day of this year in datetime
def countdown_to_congratulation(needed_datetime, additional_hours = 0):

  additional_year = is_datetime_passed(needed_datetime, additional_hours)

  birth_day_and_month = dt.datetime(dt.datetime.now().year + int(additional_year),
                                      needed_datetime.month,
                                      needed_datetime.day,
                                      additional_hours)

  return birth_day_and_month - dt.datetime.now()

# A function, that returns the substraction between this and certain year
def countdown_in_years(birthday):
  return dt.datetime.now().year - birthday.year

# A function, that is used to sort a list with kabachks
def sort_by_birthday(kabachk):
  return countdown_to_congratulation(kabachk[1]).total_seconds()

# A function, that converts a message to text and sends it to "get_time_to_next_birthday" function
def send_text_from_message(msg, message_id, bot):
  send_time_to_next_birthday(msg.text, message_id, bot)

# Changes a word's ending due to its number
def get_word_with_correct_ending(number, word_array):
  if 5 <= number % 100 <= 19:
    return word_array[2]
  if number % 10 == 1:
    return word_array[0]
  if 2 <= number % 10 <= 4:
    return word_array[1]

# Sends time to next birthday
def send_time_to_next_birthday(name, message_id, bot):
  try:
    birthday = kab.kabachks[name][1]
  except Exception as e:
    bot.send_message(message_id, "Під час обробки імені сталась помилка, скоріше за все такого імені немає у списку")
    return

  first_part_of_message = "{name} народився {day:02d}.{month:02d}.{year}.".format(name = name,
                                                                          day = birthday.day,
                                                                          month = birthday.month,
                                                                          year = birthday.year)
    
  days_to_birthday = countdown_to_congratulation(birthday).days

  days_text = get_word_with_correct_ending(days_to_birthday, ["день","дні","днів"])

  second_part_of_message = "До дня народження залишилось {days} {days_text}.".format(days = days_to_birthday, days_text = days_text)

  msg = ' '.join([first_part_of_message, second_part_of_message])
  remove_keyboard = types.ReplyKeyboardRemove()
  bot.send_message(message_id, msg, reply_markup=remove_keyboard)

# Send the congratulation message at a certain time
async def wait_to_next_birthday_and_congratulate(message_chat_id, bot, sorted_kabachks):
  for tag, birthday, _ in sorted_kabachks:
    countdown = countdown_to_congratulation(birthday, 10).total_seconds()
    
    await asyncio.sleep(countdown)
    
    years = countdown_in_years(birthday)

    years_text = get_word_with_correct_ending(years, ["рік", "роки", "років"])

    congratulate =  "Сьогодні {tag} постарішав на один рік\n"\
                    "Тепер цьому чоловіку {years} {years_text}\n"\
                    "Вітаю тебе з цим прекрасним днем від імені цього "\
                    "бота".format(tag = tag, years=years, years_text = years_text)

    bot.send_message(message_chat_id, kab.inline_notify_add(congratulate), "MarkdownV2")

# Send the scheduled congratulation message to the group
def congratulations(message_chat_id, bot):
  sorted_kabachks = sorted(kab.kabachks.values(), key = sort_by_birthday)
  asyncio.run(wait_to_next_birthday_and_congratulate(message_chat_id, bot, sorted_kabachks))