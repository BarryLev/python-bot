import datetime as dt

kabachks = {}
kabachks["Славік"] = ("@slavonch", dt.datetime(2001, 4, 23), "618621657")
kabachks["Ланс"] = ("@Lawwwyy", dt.datetime(2003, 3, 19), "282838803")
kabachks["Ваня"] = ("@Vanish229", dt.datetime(2001, 5, 29), "405203399")
kabachks["Андрюха"] = ("@Andruhe", dt.datetime(2000, 12, 3), "679322929")
kabachks["Олег"] = ("@oleh0205", dt.datetime(2002, 7, 5), "509105254")
kabachks["Роман"] = ("@MrRomchus", dt.datetime(2001, 5, 7), "321085878")
kabachks["Сергій"] = ("@Iceberg_01", dt.datetime(2001, 1, 25), "448285712")
kabachks["Вова"] = ("@johan_de_matan", dt.datetime(2001, 5, 9), "660907929")
kabachks["Мішон"] = ("@ferellugo", dt.datetime(2000, 4, 3), "514963253")
kabachks["Артем"] = ("@Slendi505", dt.datetime(2000, 5, 21), "511396241")
kabachks["Назік"] = ("@Sneaky_ZZ", dt.datetime(2000, 10, 27), "387310399")
kabachks["Ніка"] = ("@LuunaNueva", dt.datetime(2001, 5, 29), "532513465")

def get_kabachks():
  return ', '.join([tag for tag, _, _ in kabachks.values()])

def inline_notify_add(message):
  for _, _, id in kabachks.values():
    message = message + "[](tg://user?id={id})".format(id)
  return message