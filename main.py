import datetime
def get_days_from_today(date):
    try:
        target_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.date.today()
        delta = current_date - target_date


        return delta.days

    except ValueError:
        return "Неправильний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'."


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2021-05-05"))
print(get_days_from_today("wrong-date"))

