FILE_NAME = "students.txt"


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter Student Name: ")

    marks1 = float(input("Enter Marks of Subject 1: "))
    marks2 = float(input("Enter Marks of Subject 2: "))
    marks3 = float(input("Enter Marks of Subject 3: "))

    total = marks1 + marks2 + marks3
    percentage = total / 3

    grade = calculate_grade(percentage)

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{percentage:.2f},{grade}\n")

    print("\n✅ Student Record Saved Successfully!")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No Records Found!")
            return

        print("\n===== STUDENT RECORDS =====")

        for record in records:
            name, percentage, grade = record.strip().split(",")

            print(f"Name: {name}")
            print(f"Percentage: {percentage}%")
            print(f"Grade: {grade}")
            print("-" * 25)

    except FileNotFoundError:
        print("No Records Found!")


while True:
    print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
