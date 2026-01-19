# Expense Tracker - Core Python Project
# Author: Kamaleshwaran K J

import csv
import os

FILE_NAME = "expenses.csv"
expenses = []


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append({
                "amount": float(row["amount"]),
                "category": row["category"],
                "note": row["note"]
            })


def save_expense(expense):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["amount", "category", "note"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense)


def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        note = input("Enter note: ")

        expense = {
            "amount": amount,
            "category": category,
            "note": note
        }

        expenses.append(expense)
        save_expense(expense)

        print("✅ Expense added & saved successfully!")

    except ValueError:
        print("❌ Amount must be a number!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['note']}")


def category_summary():
    if not expenses:
        print("No expenses to summarize.")
        return

    summary = {}

    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\n--- Category Summary ---")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total}")


def main():
    load_expenses()

    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("👋 Exiting Expense Tracker")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
1