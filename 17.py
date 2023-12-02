import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

new_record = {"name": "Ali", "code": 40318, "job": "Database Admin"}
new_record = tuple(new_record.values())

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()


def save(record):
    command = f"INSERT INTO employees(name,code,job) VALUES {(record[0], record[1], record[2])};"
    # print(command)
    cur.execute(command)


users = [i[1:] for i in records]

# for i in users :
#     print(i)

if new_record in users:
    print("User already exists in db")
else:
    save(new_record)
    print("User added to database")

# cur.execute("SELECT * FROM employees;")
# records = cur.fetchall()

for i in records:
    print(i)

print(len(records), "Users exist in db")

con.commit()
con.close()
