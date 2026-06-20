import csv

FILE_NAME = "expenses.csv"


def create_sample_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])
            writer.writerow(["Food", 500])
            writer.writerow(["Travel", 1200])
            writer.writerow(["Shopping", 2500])
            writer.writerow(["Food", 300])

    except FileExistsError:
        pass


def analyze_expenses():
    total = 0
    highest_expense = 0
    highest_category = ""

    category_totals = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            total += amount

            if amount > highest_expense:
                highest_expense = amount
                highest_category = category

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\n===== EXPENSE REPORT =====")
    print(f"Total Spending: ₹{total:.2f}")

    print(
        f"Highest Expense: ₹{highest_expense:.2f} ({highest_category})"
    )

    print("\nCategory Wise Spending:")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


create_sample_file()

while True:
    print("\n===== CSV EXPENSE ANALYZER =====")
    print("1. Analyze Expenses")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        analyze_expenses()

    elif choice == "2":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")import csv

FILE_NAME = "expenses.csv"


def create_sample_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])
            writer.writerow(["Food", 500])
            writer.writerow(["Travel", 1200])
            writer.writerow(["Shopping", 2500])
            writer.writerow(["Food", 300])

    except FileExistsError:
        pass


def analyze_expenses():
    total = 0
    highest_expense = 0
    highest_category = ""

    category_totals = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            total += amount

            if amount > highest_expense:
                highest_expense = amount
                highest_category = category

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\n===== EXPENSE REPORT =====")
    print(f"Total Spending: ₹{total:.2f}")

    print(
        f"Highest Expense: ₹{highest_expense:.2f} ({highest_category})"
    )

    print("\nCategory Wise Spending:")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


create_sample_file()

while True:
    print("\n===== CSV EXPENSE ANALYZER =====")
    print("1. Analyze Expenses")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        analyze_expenses()

    elif choice == "2":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
