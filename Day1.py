from datetime import datetime

name = input("Enter your name: ")
birth_date = input("Enter your birth date (DD/MM/YYYY): ")

try:
    dob = datetime.strptime(birth_date, "%d/%m/%Y")
    today = datetime.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print("\n----- Age Details -----")
    print("Name:", name)
    print("Date of Birth:", dob.strftime("%d/%m/%Y"))
    print("Current Age:", age, "years")

except ValueError:
    print("Invalid date format. Please use DD/MM/YYYY.")
