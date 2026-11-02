
from app.expense_tools import Expense


def test_valid_expense():
    expense = Expense(
        amount=500,
        category="Food",
        description="Groceries"
    )

    assert expense.amount == 500
    assert expense.category == "Food"


def test_negative_expense():
    try:
        Expense(
            amount=-100,
            category="Food",
            description="Groceries"
        )
        assert False, "Negative amount should fail"

    except ValueError:
        assert True
