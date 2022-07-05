import threading as th
import datetime as dt
import kabachks as kab
import asyncio

sorted_kabachks = {}

# A function, that returns a time to certain month and day of this year in seconds
def countdown_to_congratulation(needed_datetime, additional_year = False):
  birth_day_and_month = dt.datetime(dt.datetime.now().year + int(additional_year),
                                      needed_datetime.month,
                                      needed_datetime.day,
                                      13)
  return (birth_day_and_month - dt.datetime.now()).total_seconds()

def countdown_in_years(birthday):
  return dt.datetime.now().year - birthday.year

def sort_by_birthday(kabachk):
  countdown = countdown_to_congratulation(kabachk[1])
  if countdown < 0:
    countdown = countdown_to_congratulation(kabachk[1], True)
  return countdown

async def wait_to_next_birthday_and_congratulate(message_chat_id, bot):
  for tag, birthday, _ in sorted_kabachks:
    countdown = countdown_to_congratulation(birthday)
    if countdown < 0:
      countdown = countdown_to_congratulation(birthday, True)
    await asyncio.sleep(countdown)
    
    congratulate =  "Сьогодні {tag} постарішав на один рік.\n"\
                  "Тепер цьому чоловіку {years} років. "\
                  "Вітаю тебе з цим прекрасним днем від імені цього "\
                  "бота ".format(tag = tag, years=countdown_in_years(birthday))

    congratulate = kab.inline_notify_add(congratulate)

    bot.send_message(message_chat_id, congratulate, "MarkdownV2")

# Send the scheduled congratulation message to the group
def congratulations(message_chat_id, bot):
  global sorted_kabachks
  sorted_kabachks = sorted(kab.kabachks.values(), key = sort_by_birthday)
  asyncio.run(wait_to_next_birthday_and_congratulate(message_chat_id, bot))