import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY,
name VARCHAR(50),
code INT,
job VARCHAR(70)
);
""")

students = [
    {"name": "Amirali", "code": "40211", "job": "Backend Developer"},
    {"name": "Parsa", "code": "40212", "job": "Frontend Developer"},
    {"name": "Mehrzad", "code": "40213", "job": "Security Engineer"},
    {"name": "Mohammad Mehdi", "code": "40214", "job": "DevOps Engineer"},
    {"name": "Bahar", "code": "40215", "job": "Civil Engineer"},
    {"name": "Mehrdad", "code": "40216", "job": "Data Engineer"},
]

# for person in students:
#     cur.execute(f"INSERT INTO employees(name,code,job) VALUES (?,?,?)", (person['name'], person['code'], person['job']))

# cur.execute(f"INSERT INTO employees(name,code,job) VALUES ('Ahora','40223','Project Manager')")

# cur.execute("DELETE FROM employees;")

# cur.execute("SELECT * FROM employees WHERE id=4;")
cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
for i in records:
    # if i[2] == 40213:
    #     print(i)
    print(i)
# print(records)

con.commit()
con.close()
print('Done')
