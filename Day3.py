import os

FILENAME = "expenses.txt"

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Expense Name: ")
        amount = float(input("Amount: "))

        with open(FILENAME, "a") as file:
            file.write(f"{item},{amount}\n")

        print("Expense Added Successfully!")

    elif choice == "2":
        if not os.path.exists(FILENAME):
            print("No expenses found.")
            continue

        print("\n--- Expense List ---")

        with open(FILENAME, "r") as file:
            for line in file:
                item, amount = line.strip().split(",")
                print(f"{item} - ₹{amount}")

    elif choice == "3":
        total = 0

        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as file:
                for line in file:
                    _, amount = line.strip().split(",")
                    total += float(amount)

        print(f"\nTotal Spending: ₹{total}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
