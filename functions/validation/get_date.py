from datetime import datetime

def getDate(date) -> datetime:
    day = date.day()
    month = date.month()
    year = date.year()

    return datetime(year, month, day)