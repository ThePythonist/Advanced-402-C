import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS customers (name,city,phone);")

# cur.execute("INSERT INTO customers VALUES ('Mohsen','Tehran','09334438725');")
# cur.execute("INSERT INTO customers VALUES ('Sara','Yazd','09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Ali','Bandar Anzali','09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Ghazal','Kerman','09213378325');")

cur.execute("SELECT * FROM customers;")
records = cur.fetchall()

for i in records:
    print(i)

con.commit()
con.close()
print('Done')
