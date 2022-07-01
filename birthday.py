import threading as th
import datetime as dt

def congratulate_kabachk(kabachok, message_id):
  years = dt.datetime.now().year - kabachok[1].year

  congratulate =  "Сьогодні {tag} постарішав на один рік.\n"\
                  "Тепер цьому чоловіку {years} років. "\
                  "Вітаю тебе з цим прекрасним днем від імені цього "\
                  "бота".format(tag = kabachok[0], years=years)

  