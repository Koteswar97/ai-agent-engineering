import json
from pathlib import Path
from datetime import datetime
from pydantic import BaseModel, Field
from itertools import count

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "expenses.json"
_id_counter = count(1)
class Expense(BaseModel):
    id:int = Field(default_factory=lambda:next(_id_counter))
    amount:float = Field(gt=0, description="The amount of the expense, must be greater than 0"  )
    category:str = Field(min_length=2, max_length=100, description="The category of the expense")
    description:str = Field(min_length=2, max_length=255, description="A brief description of the expense")
    date:str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"), description="The date of the expense in YYYY-MM-DD format")
    priority: str = Field(default="medium") 

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

def add_expense(expObj:Expense) -> dict:
    # expense = Expense(amount=amount, category=category, description=description,priority=priority)
    print('expObj',expObj)
    expenses = load_expenses()
    # expense_dict = expObj.model_dump()
    # print('expense_dict',expense_dict)
    # expenses.append(expense_dict)
    # save_expenses(expenses)
    expense_dict = expObj.model_dump(mode="json")
    expense_dict["id"] = max(
    (item.get("id", 0) for item in expenses),
    default=0,
) + 1
    print('Formatted expense dict:', expense_dict)
    expenses.append(expense_dict)
    print('expenses =>',expenses)
    save_expenses(expenses)

    return {
        "success": True,
        "message": "Expense added successfully",
    }
def list_expenses() -> list[dict]:
    return load_expenses()

# 6. Calculate total expenses
def get_total_expenses() -> float:
    expenses = load_expenses()

    return sum(
        expense["amount"] for expense in expenses
    )
# get Expenses by category
def get_expenses_by_category(category:str) -> list[dict]:
    expenses = load_expenses()
    print('expenses',expenses)
    return [exp for exp in expenses if exp['category'].lower() == category.lower()]

def search_anything(anySearch:str) -> list[dict]:
    expenses = load_expenses()
    anySearchItem = anySearch.lower()
    return [exp for exp in expenses if any(anySearchItem in str(val).lower() for val in exp.values()) ]

def total_expense_by_month(month:str) -> float:
     expenses = load_expenses()
     result = [exp for exp in expenses if any(month in str(val).lower() for val in exp.values()) ]
     print('results',result)
     return sum(totalVal["amount"] for totalVal in result)

def calculate_expense_total(*args):
    total = 0
    for val in args:
        total = total + val
    return total

# def print_bill():
#      print("🧾 Receipt: ₹500 for Dinner")

def new_print_bill(func):
    def wrapper():
        print('*** start ****')
        func()
        print('**** End ****')
    return wrapper
