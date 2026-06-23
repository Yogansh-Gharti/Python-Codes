import csv
import os

FILE_NAME = "employees.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["ID", "Name", "Department", "Salary"]
            )


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Monthly Salary: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [emp_id, name, department, salary]
        )

    print("✅ Employee Added Successfully!")


def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n===== EMPLOYEE RECORDS =====")
            next(reader)

            for row in reader:
                print(
                    f"🆔 {row[0]} | 👤 {row[1]} | 🏢 {row[2]} | ₹{row[3]}"
                )

    except FileNotFoundError:
        print("No Employee Records Found!")


def generate_payslip():
    emp_id = input("Enter Employee ID: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            found = False

            for row in reader:
                if row["ID"] == emp_id:

                    salary = float(row["Salary"])
                    bonus = salary * 0.10
                    total_salary = salary + bonus

                    print("\n===== PAYSLIP =====")
                    print(f"Employee ID : {row['ID']}")
                    print(f"Name        : {row['Name']}")
                    print(f"Department  : {row['Department']}")
                    print(f"Base Salary : ₹{salary:.2f}")
                    print(f"Bonus (10%) : ₹{bonus:.2f}")
                    print(
                        f"Total Salary: ₹{total_salary:.2f}"
                    )

                    found = True

            if not found:
                print("❌ Employee Not Found!")

    except FileNotFoundError:
        print("No Employee Records Found!")


initialize_file()

while True:
    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Generate Payslip")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        generate_payslip()

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
