import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()


def create_table(table_name):
    fields = input(f"Enter fields for {table_name} (seperated by comma): ").split(",")
    fields = tuple(fields)
    command = f"CREATE TABLE {table_name} {fields};"
    print(command)

    # for i in fields:
    #     open(f"{table_name}.txt", "a+").write(i + "\n")

    cur.execute(command)

    con.commit()
    con.close()
    print("Done")


def insert(table):
    pass


def select(table):
    command = f'SELECT * FROM {table};'
    cur.execute(command)
    records = cur.fetchall()
    print(records)
    con.commit()
    con.close()
    print("Done")


operation = input("""
1 : Create Table
2 : Insert Record Into Table
3 : Select Data From Table
: """)

if operation == "1":
    table_name = input("Enter table name : ")
    create_table(table_name)
elif operation == "2":
    table_name = input("Enter table name : ")
    insert(table_name)
elif operation == "3":
    table_name = input("Enter table name : ")
    select(table_name)
