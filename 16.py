import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students (name,major,grade);")

students = [
    {"name": "Amirali", "major": "Computer Engineering", "grade": "17.30"},
    {"name": "Hamed", "major": "Computer Engineering", "grade": "13.35"},
    {"name": "Pedram", "major": "Civil Engineering", "grade": "16.50"},
    {"name": "Sarina", "major": "Chemistry", "grade": "19.10"},
    {"name": "Kiana", "major": "Biology", "grade": "14.25"},
]

def insert(name, major, grade):
    command = f"INSERT INTO students VALUES {(name, major, grade)} ;"
    cur.execute(command)

def select():
    command = "SELECT * FROM students;"
    cur.execute(command)
    records = cur.fetchall()
    for i in records:
        # print(i)
        if float(i[2]) > 17 :
            print(i)
# for i in students:
#     insert(i['name'], i["major"], i["grade"])

select()

con.commit()
con.close()
print('Done')
