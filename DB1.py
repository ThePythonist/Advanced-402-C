import sqlite3

con = sqlite3.connect('Shop.db')
cur = con.cursor()

# cur.execute("DROP TABLE Product;")
cur.execute("CREATE TABLE Product (name, price, code, category);")

# cur.execute("INSERT INTO customers VALUES ('Mohsen','23','09334438725');")
# cur.execute("INSERT INTO customers VALUES ('Sara','24','09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Ali','17','09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Ghazal','13','09213378325');")

# cur.execute("DELETE FROM customers;")  # Deletes every record in table
# cur.execute("DELETE FROM customers WHERE age<'18';")

# cur.execute("DROP TABLE customers;") # Deletes table

# cur.execute("SELECT * FROM customers;")
# records = cur.fetchall()
# for i in records:
#     print(i)
# print(records)

con.commit()
con.close()
print('Done')
