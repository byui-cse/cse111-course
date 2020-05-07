import csv
from datetime import date, datetime


def main():
    # Read the CSV file into a list of lists.
    player_list = []
    with open("soccer.csv", "rt") as infile:
        reader = csv.reader(infile)
        for row in reader:
            if reader.line_num == 1:
                headings = row
            else:
                row[2] = strpdate(row[2])
                player_list.append(row)

    # Create the cutoff date to be
    # Aug 1 during the current year.
    curr_year = date.today().year
    cutoff = date(curr_year, 8, 1)
    print(cutoff)

    age_at_cutoff(player_list, cutoff)

    print(year_diff(strpdate("2013-02-28"), strpdate("2016-02-29")))
    print(year_diff(strpdate("2016-02-29"), strpdate("2019-02-28")))
    print(year_diff(strpdate("2016-02-29"), strpdate("2019-03-01")))


def strpdate(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


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


def age_at_cutoff(player_list, cutoff):
    for row in player_list:
        birthday = row[2]
        print(year_diff(birthday, cutoff))


main()
