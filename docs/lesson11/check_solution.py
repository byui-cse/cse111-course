from datetime import datetime

def main():
    #years = [1995, 2000, 1998, 2013, 2014, 2001, 2002, 2004, 2002, 1997]
    #months = [1, 2, 4, 7, 7, 5, 8, 12, 11, 9]
    #days = [4, 8, 1, 17, 21, 23, 28, 30, 15, 17]

    #str_dates = []
    #for year, month, day in zip(years, months, days):
    #    str_dates.append(f"{year}-{month:02d}-{day:02d}")
    #str_dates = sorted(str_dates)
    #print(str_dates)


    strings = [
        "1995-01-04", "1997-09-17", "1998-04-01", "2000-02-08",
        "2001-05-23", "2002-08-28", "2002-11-15", "2004-12-30",
        "2013-07-17", "2014-07-21"
    ]
    dates = list(map(strpdate, strings))
    #today = [datetime.today().date() for _ in range(len(dates))]
    #ages = list(map(year_diff, dates, today))
    ages = list(map(curr_age, dates))
    print(ages)


def strpdate(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def curr_age(birthdate):
    today = datetime.today().date()
    return year_diff(birthdate, today)

def year_diff(before, after):
    if before > after:
        swap = before
        before = after
        after = swap

    years = after.year - before.year
    if before.month > after.month or \
        (before.month == after.month and before.day > after.day):
        years -= 1
    return years


main()
