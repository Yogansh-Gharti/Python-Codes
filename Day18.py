import csv
import os

FILE_NAME = "donors.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Blood Group", "Contact", "City"])


def add_donor():
    name = input("Enter Donor Name: ")
    blood_group = input("Enter Blood Group (A+, B+, O+, etc.): ").upper()
    contact = input("Enter Contact Number: ")
    city = input("Enter City: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, blood_group, contact, city])

    print("✅ Donor Added Successfully!")


def view_donors():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n===== DONOR LIST =====")
            next(reader)

            for row in reader:
                print(
                    f"👤 {row[0]} | 🩸 {row[1]} | 📞 {row[2]} | 📍 {row[3]}"
                )

    except FileNotFoundError:
        print("No Donor Records Found!")


def search_blood_group():
    blood_group = input(
        "Enter Required Blood Group: "
    ).upper()

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            found = False

            print("\n===== MATCHING DONORS =====")

            for row in reader:
                if row["Blood Group"] == blood_group:
                    print(
                        f"👤 {row['Name']} | 📞 {row['Contact']} | 📍 {row['City']}"
                    )
                    found = True

            if not found:
                print("❌ No Matching Donors Found!")

    except FileNotFoundError:
        print("No Donor Records Found!")


initialize_file()

while True:
    print("\n===== BLOOD DONATION MANAGEMENT SYSTEM =====")
    print("1. Add Donor")
    print("2. View All Donors")
    print("3. Search by Blood Group")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_donor()

    elif choice == "2":
        view_donors()

    elif choice == "3":
        search_blood_group()

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
