import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Load expenses from CSV
def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "date": row["Date"],
                    "category": row["Category"],
                    "amount": float(row["Amount"]),
                    "description": row["Description"]
                })
    return expenses

# Save expenses to CSV
def save_expenses(expenses):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for expense in expenses:
            writer.writerow([
                expense["date"],
                expense["category"],
                expense["amount"],
                expense["description"]
            ])

# Add a new expense
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD) [Press Enter for today]: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    category = input("Enter category (Food, Travel, Shopping, etc.): ")

    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            break
        except ValueError:
            print("Please enter a valid number.")

    description = input("Enter description: ")

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })

    save_expenses(expenses)
    print("\nExpense added successfully!\n")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n{:<12} {:<15} {:<10} {}".format(
        "Date", "Category", "Amount", "Description"))
    print("-" * 55)

    for expense in expenses:
        print("{:<12} {:<15} ₹{:<9.2f} {}".format(
            expense["date"],
            expense["category"],
            expense["amount"],
            expense["description"]
        ))

# Show total expense
def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}\n")

# Category-wise summary
def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\nCategory Summary")
    print("-" * 30)
    for category, amount in summary.items():
        print(f"{category:<15} ₹{amount:.2f}")

# Main Menu
def main():
    expenses = load_expenses()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
