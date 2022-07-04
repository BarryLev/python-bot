import threading as th
import datetime as dt
import kabachks as kab

def congratulate_kabachk(kabachok, chat_id, bot):
  years = dt.datetime.now().year - kabachok[1].year

  congratulate =  "Сьогодні {tag} постарішав на один рік.\n"\
                  "Тепер цьому чоловіку {years} років. "\
                  "Вітаю тебе з цим прекрасним днем від імені цього "\
                  "бота".format(tag = kabachok[0], years=years)

  bot.send_message(chat_id, congratulate)

# A function, that returns a time to certain month and day of this year in seconds
def countdown_to_congratulation(needed_datetime, additional_year = False):
  birth_day_and_month = dt.datetime(dt.datetime.now().year + int(additional_year),
                                      needed_datetime.month,
                                      needed_datetime.day,
                                      10)
  return (birth_day_and_month - dt.datetime.now()).total_seconds()

# Send the scheduled congratulation message to the group
def congratulations(message_chat_id, bot):
  for kabachk in kab.kabachks.values():
    time_to_run = countdown_to_congratulation(kabachk[1])
    if time_to_run < 0:
      time_to_run = countdown_to_congratulation(kabachk[1], True) # If the countdown is negative(this date has passed in this year), the function will execute in the next year
    
    th.Timer( time_to_run,
              congratulate_kabachk,
              [kabachk, message_chat_id, bot]).start()