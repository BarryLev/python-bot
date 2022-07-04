import threading as th
import datetime as dt
import kabachks as kab

sorted_kabachks = {}

# def congratulate_kabachk(kabachok, chat_id, bot):
#   years = dt.datetime.now().year - kabachok[1].year

#   congratulate =  "Сьогодні {tag} постарішав на один рік.\n"\
#                   "Тепер цьому чоловіку {years} років. "\
#                   "Вітаю тебе з цим прекрасним днем від імені цього "\
#                   "бота".format(tag = kabachok[0], years=years)

#   bot.send_message(chat_id, congratulate)

# A function, that returns a time to certain month and day of this year in seconds
def countdown_to_congratulation(needed_datetime, additional_year = False):
  birth_day_and_month = dt.datetime(dt.datetime.now().year + int(additional_year),
                                      needed_datetime.month,
                                      needed_datetime.day,
                                      10)
  return (birth_day_and_month - dt.datetime.now()).total_seconds()

def sort_by_birthday(kabachk):
  countdown = countdown_to_congratulation(kab.kabachks[kabachk][1])
  if countdown < 0:
    countdown = countdown_to_congratulation(kab.kabachks[kabachk][1], True)
  print(countdown)
  return countdown

# Send the scheduled congratulation message to the group
def congratulations(message_chat_id, bot):
  global sorted_kabachks
  sorted_kabachks = sorted(kab.kabachks, key = sort_by_birthday)
  