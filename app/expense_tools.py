import json
from pathlib import Path
from datetime import datetime
from pydantic import BaseModel, Field

DATA_FILE = Path("data/expenses.json")

class Expense(BaseModel):
    amount:float = Field(gt=0, description="The amount of the expense, must be greater than 0"  )
    category:str = Field(min_length=2, max_length=100, description="The category of the expense")
    description:str = Field(min_length=2, max_length=255, description="A brief description of the expense")
    date:str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"), description="The date of the expense in YYYY-MM-DD format")

# Read expenses from the JSON file
def load_expenses() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_expenses(expenses: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount: float, category: str, description: str) -> dict:
    expense = Expense(amount=amount, category=category, description=description)
    expenses = load_expenses()
    expenses.append(expense.model_dump())
    save_expenses(expenses)
    return {
        "success": True,
        "message": "Expense added successfully",
        "expense": expense.model_dump()
    }
def list_expenses() -> list[dict]:
    return load_expenses()

# 6. Calculate total expenses
def get_total_expenses() -> float:
    expenses = load_expenses()

    return sum(
        expense["amount"] for expense in expenses
    )