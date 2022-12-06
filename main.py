from datetime import timedelta, datetime


def next_day(y, m, d):
    day_from_user = datetime(y, m, d)
    day_next = day_from_user + timedelta(days=1)
    date_next = str(day_next)
    return date_next[:10]


year = int(input("Podaj rok: "))
month = int(input("Podaj miesiąc [1-12]: "))
day = int(input("Podaj dzień [1-30]: "))


print(f"Kolejny dzień po podanej dacie to {next_day(year, month, day)}")
