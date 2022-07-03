import threading as th
import datetime as dt

def calculate_countdown(kabachok):
  return dt.datetime(dt.datetime.now().year + 1,
                                      kabachok.month,
                                      kabachok.day,
                                      10).total_seconds()

def congratulate_kabachk(kabachok, chat_id, bot):
  years = dt.datetime.now().year - kabachok[1].year

  congratulate =  "Сьогодні {tag} постарішав на один рік.\n"\
                  "Тепер цьому чоловіку {years} років. "\
                  "Вітаю тебе з цим прекрасним днем від імені цього "\
                  "бота".format(tag = kabachok[0], years=years)

  bot.send_message(chat_id, "Починаю свою роботу")

  th.Timer( calculate_countdown(kabachok),
            congratulate_kabachk,
            [kabachok, chat_id, bot]).start()