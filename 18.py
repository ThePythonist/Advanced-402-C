import sqlite3


def create_table(table_name):
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    fields = input(f"Enter fields for {table_name} (seperated by comma): ").split(",")
    fields = tuple(fields)
    command = f"CREATE TABLE {table_name} {fields};"
    # print(command)

    # for i in fields:
    #     open(f"{table_name}.txt", "a+").write(i + "\n")

    cur.execute(command)

    con.commit()
    con.close()
    print("Done")

    print()
    main()


def select(table):
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    command = f"PRAGMA table_info({table});"
    cur.execute(command)
    columns = cur.fetchall()

    command = f'SELECT * FROM {table};'
    cur.execute(command)
    values = cur.fetchall()
    fields = []
    for i in range(len(columns)):
        fields.append(columns[i][1])

    records = []
    for i in values:
        records.append(dict(zip(fields, i)))

    for i in records:
        print(i)

    print()
    main()


def insert(table):
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    command = f"PRAGMA table_info({table});"
    cur.execute(command)
    columns = cur.fetchall()
    values = []

    for i in range(len(columns)):
        entry = input(f"{columns[i][1]} : ")
        values.append(entry)

    command = f"INSERT INTO {table} VALUES {tuple(values)};"
    cur.execute(command)
    con.commit()
    con.close()
    print("Done")

    print()
    main()


def main():
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


main()
