import jdatetime

now = str(jdatetime.datetime.now())
date = now.split()[0]
print(date[5:])
