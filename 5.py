from persiantools.jdatetime import JalaliDateTime
import pytz

now = str(JalaliDateTime.now()).split()[0].split("-")
y = int(now[0])
m = int(now[1])
d = int(now[2])
jalali = JalaliDateTime(y, m, d, 0, 0, 0, 0, pytz.utc).strftime("%A")
print(jalali)
