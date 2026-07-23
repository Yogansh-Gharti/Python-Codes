import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

conn = sqlite3.connect("finance.db")
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

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "INSERT INTO transactions(type,category,amount,date) VALUES(?,?,?,?)",
        (t, category, amount, date)
    )

    conn.commit()

    print("\n✅ Transaction Added Successfully!")


def show_summary():

    df = pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )

    if df.empty:
        print("No Data Found.")
        return

    income = df[df["type"] == "Income"]["amount"].sum()
    expense = df[df["type"] == "Expense"]["amount"].sum()

    balance = income - expense

    print("\n====== FINANCIAL SUMMARY ======")
    print(f"Total Income : ₹{income:.2f}")
    print(f"Total Expense: ₹{expense:.2f}")
    print(f"Balance      : ₹{balance:.2f}")


def pie_chart():

    df = pd.read_sql_query(
        "SELECT * FROM transactions WHERE type='Expense'",
        conn
    )

    if df.empty:
        print("No Expense Data Found.")
        return

    category = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(6,6))
    plt.pie(
        category,
        labels=category.index,
        autopct="%1.1f%%"
    )
    plt.title("Expense Distribution")
    plt.show()


def bar_chart():

    df = pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )

    if df.empty:
        print("No Data Found.")
        return

    income = df[df["type"]=="Income"]["amount"].sum()
    expense = df[df["type"]=="Expense"]["amount"].sum()

    plt.figure(figsize=(5,4))
    plt.bar(
        ["Income","Expense"],
        [income,expense]
    )

    plt.title("Income vs Expense")
    plt.ylabel("Amount")

    plt.show()


def export_excel():

    df = pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )

    df.to_excel(
        "Finance_Report.xlsx",
        index=False
    )

    print("\n✅ Excel Report Exported!")


while True:

    print("\n======= PERSONAL FINANCE DASHBOARD =======")

    print("1. Add Transaction")
    print("2. Financial Summary")
    print("3. Expense Pie Chart")
    print("4. Income vs Expense Chart")
    print("5. Export Excel Report")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_transaction()

    elif choice == "2":
        show_summary()

    elif choice == "3":
        pie_chart()

    elif choice == "4":
        bar_chart()

    elif choice == "5":
        export_excel()

    elif choice == "6":
        break

    else:
        print("Invalid Choice")

conn.close()
