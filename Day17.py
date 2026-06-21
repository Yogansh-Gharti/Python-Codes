import csv
import os

FILE_NAME = "inventory.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Product", "Price", "Stock"])


def add_product():
    product = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, price, stock])

    print("✅ Product Added Successfully!")


def view_inventory():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n===== INVENTORY =====")
        next(reader)

        for row in reader:
            print(f"📦 {row[0]} | ₹{row[1]} | Stock: {row[2]}")


def search_product():
    name = input("Enter Product Name: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            if row["Product"].lower() == name:
                print("\n===== PRODUCT FOUND =====")
                print(f"Product: {row['Product']}")
                print(f"Price: ₹{row['Price']}")
                print(f"Stock: {row['Stock']}")
                found = True

        if not found:
            print("❌ Product Not Found!")


def low_stock_alert():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== LOW STOCK PRODUCTS =====")

        found = False

        for row in reader:
            if int(row["Stock"]) < 5:
                print(
                    f"⚠️ {row['Product']} - Only {row['Stock']} Left"
                )
                found = True

        if not found:
            print("No Low Stock Products!")


initialize_file()

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Search Product")
    print("4. Low Stock Alert")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_inventory()

    elif choice == "3":
        search_product()

    elif choice == "4":
        low_stock_alert()

    elif choice == "5":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
