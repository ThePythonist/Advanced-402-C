import datetime
import jdatetime


def gregorian_age(birth):
    thisyear = int(datetime.datetime.now().year)
    age = thisyear - birth
    return age


def jalali_age(birth):
    thisyear = int(jdatetime.datetime.now().year)
    age = thisyear - birth
    return age


# show_gregorian_age(2006)
# show_jalali_age(1390)