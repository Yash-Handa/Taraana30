"""
A utility module that calculates the the date of previous Saturday
main use: naming of the follders in data directory
"""
from datetime import datetime as dt, timedelta


def saturday():
    """
    A function that returns the date of previous saturday in DD-MM-YYYY fromate

    Week changes at Sat 23:59:99999 (Mid Night)
    """
    now = dt.now()
    day_no = int(now.strftime("%w"))
    sat = now - timedelta(days=day_no + 1)
    sat = sat.strftime('%d%m%Y')
    return sat[:2] + '-' + sat[2:4] + '-' + sat[4:]


if __name__ == '__main__':
    print(saturday())
