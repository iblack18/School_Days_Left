import datetime
import pytz

def school_day(date):
    if date.weekday() == 6 and date.weekday() == 5:
        return False
    else:
        return True

def holiday(date):
    if date.month == 3:
        spring_break = range(26, 31)
        if date.day in spring_break:
            return True
        else:
            return False
    elif date.month == 4:
        # Easter Monday
        if date.day == 2:
            return True
        else:
            return False
    else:
        return False

def school_end(date):
    if date.day == 23:
        if date.month == 5:
            return True
        
def days(date):
    chicago = pytz.timezone("America/Chicago")
    date = chicago.localize(date)
    days = 0

    while True:
        date += datetime.timedelta(days=1)
        if school_day(date) == True:
            if holiday(date) == False:
                days += 1
        if school_end(date) == True:
            break
            # Senior retreat day unknown to me, will remove negative one from code when it happens
    return (days - 1)
