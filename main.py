from app.expense_tools import (
    add_expense,
    list_expenses,
    get_total_expenses
)
added_expense = add_expense(50.0, "Groceries", "Weekly grocery shopping")
print("Added Expense:", added_expense)

added_expense = add_expense(20.0, "Transport", "Bus fare")
print("Added Expense:", added_expense)
all_expenses = list_expenses()

for expense in all_expenses:
    print(f"Expense: {expense['amount']} - {expense['category']} - {expense['description']} - {expense['date']}")

total_expenses = get_total_expenses()


print(f"Total Expenses: {total_expenses}")