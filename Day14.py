FILE_NAME = "attendance.txt"


def add_student():
    name = input("Enter Student Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},0,0\n")

    print("✅ Student Added Successfully!")


def mark_attendance():
    student_name = input("Enter Student Name: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        updated_students = []
        found = False

        for student in students:
            name, present, total = student.strip().split(",")

            if name.lower() == student_name:
                present = int(present) + 1
                total = int(total) + 1

                updated_students.append(
                    f"{name},{present},{total}\n"
                )

                found = True
            else:
                updated_students.append(student)

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_students)

        if found:
            print("✅ Attendance Marked!")
        else:
            print("Student Not Found!")

    except FileNotFoundError:
        print("No Students Found!")


def mark_absent():
    student_name = input("Enter Student Name: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        updated_students = []
        found = False

        for student in students:
            name, present, total = student.strip().split(",")

            if name.lower() == student_name:
                total = int(total) + 1

                updated_students.append(
                    f"{name},{present},{total}\n"
                )

                found = True
            else:
                updated_students.append(student)

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_students)

        if found:
            print("✅ Absence Recorded!")
        else:
            print("Student Not Found!")

    except FileNotFoundError:
        print("No Students Found!")


def view_report():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No Records Found!")
            return

        print("\n===== ATTENDANCE REPORT =====")

        for student in students:
            name, present, total = student.strip().split(",")

            present = int(present)
            total = int(total)

            percentage = 0

            if total > 0:
                percentage = (present / total) * 100

            print(f"\n👨‍🎓 Student: {name}")
            print(f"✅ Present: {present}")
            print(f"📅 Total Classes: {total}")
            print(f"📊 Attendance: {percentage:.2f}%")

    except FileNotFoundError:
        print("No Records Found!")


while True:
    print("\n===== ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Present")
    print("3. Mark Absent")
    print("4. View Attendance Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        mark_absent()

    elif choice == "4":
        view_report()

    elif choice == "5":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
