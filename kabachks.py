import datetime as dt

kabachks = {}
kabachks["Славік"] = ("@slavonch", dt.datetime(2001, 4, 23))
kabachks["Ланс"] = ("@Lawwwyy", dt.datetime(2003, 3, 19))
kabachks["Ваня"] = ("@Vanish229", dt.datetime(2001, 5, 29))
kabachks["Андрюха"] = ("@Andruhe", dt.datetime(2000, 12, 3))
kabachks["Олег"] = ("@oleh0205", dt.datetime(2002, 7, 5))
kabachks["Роман"] = ("@MrRomchus", dt.datetime(2001, 5, 7))
kabachks["Сергій"] = ("@Iceberg_01", dt.datetime(2001, 1, 25))
kabachks["Вова"] = ("@johan_de_matan", dt.datetime(2001, 5, 9))
kabachks["Мішон"] = ("Ферел", dt.datetime(2000, 4, 3))
kabachks["Артем"] = ("@Slendi505", dt.datetime(2000, 5, 21))
kabachks["Назік"] = ("@Sneaky_ZZ", dt.datetime(2000, 10, 27))

def get_kabachks():
  return ', '.join(kabachks.values[0])