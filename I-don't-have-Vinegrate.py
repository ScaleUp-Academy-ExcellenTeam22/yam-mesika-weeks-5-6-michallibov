import random
import datetime
import calendar

"""
This program gets from the user two dates and generates a date between the two date. If the generated
date is Monday- the program will print 'I am out of Vinegrate', otherwise it'll print the day of that
date.
Note- you can only enter dates after the first unix epoch second which was at- 00:00:00 UTC on 1 January 1970
"""


def print_solution(day):
    """
    This function prints 'I'm out f Vinegret!' if the randed
    date's day is Monday or the day itself if the day is not
    Monday.
    :param day: the day of the randed date
    """
    if calendar.day_name[day] == 'Monday':
        print("I'm out of Vinegret!")
    else:
        print(calendar.day_name[day])


def randomize(first_timestamp, second_timestamp):
    """
    This function randomizes a number between the two timestamps which will
    be later converted to a date that is also going to be between the two
    given dates.
    :param first_timestamp: the first date we received from the user converted to timestamp
    :param second_timestamp: the second date we received from the user converted to timestamp
    :return the randomized date's day
    """

    # The first timestamp's date is before the second timestamp's date
    if first_timestamp < second_timestamp:
        randed = random.randint(first_timestamp, second_timestamp)

    # The second timestamp's date is before the first timestamp's date
    else:
        randed = random.randint(second_timestamp, first_timestamp)

    new_date = datetime.datetime.fromtimestamp(randed)
    day = datetime.datetime.weekday(new_date)
    return day


def convert_to_timestamp(first_date, second_date):
    """
    This function converts the datetime variables to timestamps.
    :param first_date: the first date we received from the user
    :param second_date:  the second date we received from the user
    :return the return value of the randomize function which is the
            randomized date's day
    """
    timestamp1 = datetime.datetime.timestamp(first_date)
    timestamp2 = datetime.datetime.timestamp(second_date)
    timestamp1 = int(timestamp1)
    timestamp2 = int(timestamp2)
    return randomize(timestamp1, timestamp2)


def convert_to_date(first_date, second_date):
    """
    This function converts a given date string to a datetime variable.
    :param first_date: the first date we received from the user in a form of string
    :param second_date: the second date we received from the user in a form of string
    """
    first_converted_date = datetime.datetime.strptime(first_date, "%Y-%m-%d")
    second_converted_date = datetime.datetime.strptime(second_date, "%Y-%m-%d")
    return convert_to_timestamp(first_converted_date, second_converted_date)


if __name__ == '__main__':
    first_date = input("Enter first date: ")
    second_date = input("Enter second date: ")
    print_solution(convert_to_date(first_date, second_date))
