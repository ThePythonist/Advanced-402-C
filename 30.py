import csv


def write_students_data(filename):
    header = ["Name", "Grade"]
    data = [
        ["Homayoon", 18.1],
        ["Hesam", 18.2],
        ["Maryam", 18.3],
        ["Mahdyar", 18.4],
        ["Matin", 18.5],
    ]

    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    print("Done")

def read_students_data(filename):
    with open(f"{filename}.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row)

# write_students_data(input("Enter a file name : "))
read_students_data(input("Enter a file name : "))