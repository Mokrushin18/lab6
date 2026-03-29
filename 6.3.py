def is_magic_date(day, month, year):
    return day * month == year % 100

date = input("Введите дату (дд.мм.гггг): ")
d, m, y = map(int, date.split("."))

print(is_magic_date(d, m, y))