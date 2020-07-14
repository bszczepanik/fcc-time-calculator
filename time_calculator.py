from datetime import datetime
from datetime import timedelta
import time
import calendar


def add_time(start, duration, *day):
    new_time = 0
    if day != ():
        day_number = list(calendar.day_name).index(day[0].capitalize())
    else:
        day_number = 0

    base_time = datetime.strptime(
        start, "%I:%M %p") + timedelta(days=day_number)
    offset_time = list(map(int, (duration.split(":"))))
    delta_time = timedelta(hours=offset_time[0], minutes=offset_time[1])
    result_time = base_time + delta_time
    days_diff = result_time.day - base_time.day

    new_time = datetime.strftime(
        result_time, "%I:%M %p").lstrip("0").replace(" 0", " ")

    if day != ():
        new_time += datetime.strftime(result_time, ", %A")

    if days_diff == 1:
        new_time += " (next day)"
    elif days_diff > 1:
        new_time += " (%i days later)" % (days_diff)

    return new_time
