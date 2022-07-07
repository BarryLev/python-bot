import threading as th
import datetime as dt
import kabachks as kab
import asyncio
import pprint as pp

sorted_kabachks = {}

# A function, that returns a time to certain month and day of this year in datetime
def countdown_to_congratulation(needed_datetime, additional_hours = 0, additional_year = False):
  birth_day_and_month = dt.datetime(dt.datetime.now().year + int(additional_year),
                                      needed_datetime.month,
                                      needed_datetime.day,
                                      additional_hours)

  time_to_birthday = birth_day_and_month - dt.datetime.now()
  
  if time_to_birthday.total_seconds() < 0:
    time_to_birthday = countdown_to_congratulation(needed_datetime, additional_hours, additional_year = True)

  return time_to_birthday

# A function, that returns the substraction between this and certain year
def countdown_in_years(birthday):
  return dt.datetime.now().year - birthday.year

# A function, that is used to sort a list with kabachks
def sort_by_birthday(kabachk):
  return countdown_to_congratulation(kabachk[1]).total_seconds()

# A function, that converts a message to text and sends it to "get_time_to_next_birthday" function
def send_text_from_message(msg, message_id, bot):
  get_time_to_next_birthday(msg.text, message_id, bot)

# 
def get_time_to_next_birthday(name, message_id, bot):
  try:
    birthday = kab.kabachks[name][1]
  except Exception as e:
    bot.send_message(message_id, "Під час обробки імені сталась помилка, скоріше за все такого імені немає у списку")
    return

  month = birthday.month
  if month / 10 == 0:
    month = "0" + str(month)

  first_part_of_message = "{name} народився {day}.{month:02d}.{year}.".format(name = name,
                                                                          day = birthday.day,
                                                                          month = birthday.month,
                                                                          year = birthday.year)
    
  countdown = countdown_to_congratulation(birthday)
  second_part_of_message = "До дня народження залишилось {days} днів.".format( days = countdown.days)

  msg = ' '.join([first_part_of_message, second_part_of_message])
  bot.send_message(message_id, msg)

async def wait_to_next_birthday_and_congratulate(message_chat_id, bot):
  for tag, birthday, _ in sorted_kabachks:
    countdown = countdown_to_congratulation(birthday, 10).total_seconds()
    
    await asyncio.sleep(countdown)
    
    years = countdown_in_years(birthday)
    if years % 10 == 1:
      years_text = "рік"
    elif years % 10 >= 2 and years % 10 <= 4:
      years_text = "роки"
    else:
      years_text = "років"

    congratulate =  "Сьогодні {tag} постарішав на один рік\n"\
                    "Тепер цьому чоловіку {years} {years_text}\n"\
                    "Вітаю тебе з цим прекрасним днем від імені цього "\
                    "бота".format(tag = tag, years=years, years_text = years_text)

    bot.send_message(message_chat_id, kab.inline_notify_add(congratulate), "MarkdownV2")

# Send the scheduled congratulation message to the group
def congratulations(message_chat_id, bot):
  global sorted_kabachks
  sorted_kabachks = sorted(kab.kabachks.values(), key = sort_by_birthday)
  asyncio.run(wait_to_next_birthday_and_congratulate(message_chat_id, bot))