import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("SELECT * FROM customers;")
records = cur.fetchall()

for i in records:
    print(i[2])

con.commit()
con.close()
print('Done')
