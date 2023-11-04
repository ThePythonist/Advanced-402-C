import datetime
import jdatetime


def show_gregorian_age(birth):
    thisyear = int(datetime.datetime.now().year)
    age = thisyear - birth
    print(age)


def show_jalali_age(birth):
    thisyear = int(jdatetime.datetime.now().year)
    age = thisyear - birth
    print(age)


# show_gregorian_age(2006)
show_jalali_age(1390)
