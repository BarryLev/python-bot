import datetime as dt
from telebot import types

kabachks = {}
kabachks["Славік"] = ("@slavonch", dt.datetime(2001, 4, 23), "618621657")
kabachks["Ланс"] = ("@Lawwwyy", dt.datetime(2003, 3, 19), "282838803")
kabachks["Ваня"] = ("@Vanish229", dt.datetime(2001, 5, 29), "405203399")
kabachks["Андрюха"] = ("@Andruhe", dt.datetime(2000, 12, 3), "679322929")
kabachks["Олег"] = ("@oleh0205", dt.datetime(2002, 7, 5), "509105254")
kabachks["Роман"] = ("@MrRomchus", dt.datetime(2001, 5, 7), "321085878")
kabachks["Сергій"] = ("@Iceberg01", dt.datetime(2001, 1, 25), "448285712") #Iceberg_01
kabachks["Вова"] = ("@johandematan", dt.datetime(2001, 5, 9), "660907929") #johan_de_matan
kabachks["Мішон"] = ("@ferellugo", dt.datetime(2000, 4, 3), "514963253")
kabachks["Артем"] = ("@Slendi505", dt.datetime(2001, 5, 21), "511396241")
kabachks["Назік"] = ("@SneakyZZ", dt.datetime(2000, 10, 27), "387310399") #Sneaky_ZZ
kabachks["Ніка"] = ("@LuunaNueva", dt.datetime(2001, 5, 29), "532513465")
# kabachks["Тест"] = ("Тест", dt.datetime.now() + dt.timedelta(seconds=20), "0")

def get_kabachks():
  return ', '.join([tag for tag, _, _ in kabachks.values()])

def inline_notify_add(message, write_tags = False):
  for tag, birthday, id in kabachks.values():
    if not write_tags:
      tag = '⠀'
    message = message + "[{tag}](tg://user?id={id}) ".format(tag = tag, id = id)
  return message

def send_list_of_kabacks():
  markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
  for name in kabachks:
    markup.add(types.KeyboardButton(name))
  return markup