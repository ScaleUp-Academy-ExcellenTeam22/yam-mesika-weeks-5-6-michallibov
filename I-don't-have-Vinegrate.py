import random
import datetime
import calendar

"""
This program gets from the user two dates and generates a date between the two date. If the generated
date is Monday- the program will print 'I am out of Vinegrate', otherwise it'll print the day of that
date.
Note- you can only enter dates after the first unix epoch second which was at- 00:00:00 UTC on 1 January 1970
"""

# This function converts the random timestamp to a date and prints the day of the week of the
# randomized date, or if it's day is monday- it will print 'I'm out of Vinegret!'.
def print_solution(randed):
    new_date = datetime.datetime.fromtimestamp(randed)
    day = datetime.datetime.weekday(new_date)

    if calendar.day_name[day] == 'Monday':
        print("I'm out of Vinegret!")
    else:
        print(calendar.day_name[day])


# This function randomizes a number between the two timestamps which will
# be later converted to a date that is also going to be between the two
# given dates.
def randomize(timestamp1, timestamp2):
    if timestamp1 < timestamp2:     # the first timestamp's date is before the second timestamp's date
        randed = random.randint(timestamp1, timestamp2)
    else:                           # the second timestamp's date is before the first timestamp's date
        randed = random.randint(timestamp2, timestamp1)
    print_solution(randed)


# This function converts the datetime variables to timestamps.
def convert_to_timestamp(date1, date2):
    timestamp1 = datetime.datetime.timestamp(date1)
    timestamp2 = datetime.datetime.timestamp(date2)
    timestamp1 = int(timestamp1)
    timestamp2 = int(timestamp2)
    randomize(timestamp1, timestamp2)


# This function converts a given date string to a datetime variable.
def convert_to_date(f_date, s_date):
    date1 = datetime.datetime.strptime(f_date, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(s_date, "%Y-%m-%d")
    convert_to_timestamp(date1, date2)


first_date = input("Enter first date: ")
second_date = input("Enter second date: ")
convert_to_date(first_date, second_date)