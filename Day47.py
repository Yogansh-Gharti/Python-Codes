import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    category TEXT,
    amount REAL,
    date TEXT
)
""")

conn.commit()


def add_transaction():
    t = input("Type (Income/Expense): ").capitalize()
    category = input("Category: ")
    amount = float(input("Amount: "))

    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cursor.execute(
        "INSERT INTO transactions(type, category, amount, date) VALUES(?,?,?,?)",
        (t, category, amount, date)
    )

    conn.commit()

    print("\n✅ Transaction Added Successfully!")


def view_transactions():

    cursor.execute("SELECT * FROM transactions")

    rows = cursor.fetchall()

    if not rows:
        print("\nNo Transactions Found.")
        return

    print("\n========== TRANSACTIONS ==========\n")

    for row in rows:
        print(row)


def filter_category():

    category = input("Enter Category: ")

    cursor.execute(
        "SELECT * FROM transactions WHERE category=?",
        (category,)
    )

    rows = cursor.fetchall()

    if not rows:
        print("\nNo Records Found.")
        return

    print()

    for row in rows:
        print(row)


def summary():

    cursor.execute(
        "SELECT SUM(amount) FROM transactions WHERE type='Income'"
    )

    income = cursor.fetchone()[0] or 0

    cursor.execute(
        "SELECT SUM(amount) FROM transactions WHERE type='Expense'"
    )

    expense = cursor.fetchone()[0] or 0

    balance = income - expense

    print("\n========= SUMMARY =========")
    print(f"Total Income : ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Balance      : ₹{balance}")


def export_csv():

    df = pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )

    df.to_csv(
        "transactions.csv",
        index=False
    )

    print("\n✅ Exported to transactions.csv")


while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Filter by Category")
    print("4. Financial Summary")
    print("5. Export to CSV")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_transaction()

    elif choice == "2":
        view_transactions()

    elif choice == "3":
        filter_category()

    elif choice == "4":
        summary()

    elif choice == "5":
        export_csv()

    elif choice == "6":
        break

    else:
        print("Invalid Choice")

conn.close()