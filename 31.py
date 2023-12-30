import csv


def write_students_data(filename):
    header = ["Name", "Field"]
    data = [
        ["Homayoon", "Computer Engineering"],
        ["Hesam", "Accouting"],
        ["Maryam", "Electrical Engineering"],
        ["Mahdyar", "Computer Science"],
        ["Matin", "MBA"],
    ]

    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    print("Done")

def find_students(filename):
    keyword = "computer"
    with open(f"{filename}.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            field = row[1]
            if keyword in field.lower():
                print(row)

# write_students_data(input("Enter a file name : "))
find_students(input("Enter a file name : "))
