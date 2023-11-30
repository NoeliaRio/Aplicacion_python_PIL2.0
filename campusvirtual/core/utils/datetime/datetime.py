from datetime import datetime, timedelta, time

def first_day_of_week():
    """
    Primer día habil de la semana (lunes)
    """
    first_day_of_week = datetime.today() - timedelta(days=datetime.today().weekday())
    first_day_of_week = datetime.combine(first_day_of_week.date(), time(0,0,0))
    return first_day_of_week

def last_day_of_week():
    """
    Último día habil de la semana (viernes)
    """
    last_day_of_week = first_day_of_week() + timedelta(days=4)
    last_day_of_week = datetime.combine(last_day_of_week.date(), time(23,59,59))
    return last_day_of_week

def last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) + timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return datetime.date(next_month - timedelta(days=next_month.day))

def first_day_of_month(any_day):
    return datetime.date(any_day.replace(day=1))