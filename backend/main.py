from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Literal
from app.expense_tools import add_expense, list_expenses, save_expenses
app = FastAPI(title="Expense tracker API")

class Expenses(BaseModel):
    category: str = Field(min_length=4,max_length=15)
    description:str = Field(max_length=200, min_length=10)
    amount:float = Field(default=0.0, lt=100000)
    date:Optional[datetime] = Field(default=lambda: datetime.now().strftime("%Y-%m-%d"))
    priority:Literal['low','medium','high'] = Field(default='medium')

class ExpenseOutput(BaseModel):
    category:str
    description:str
    priority:str


    
@app.get("/")
def home():
    return {"Message":"Welcome to Expense tracker API is running"}

@app.post("/addExpense",response_model=ExpenseOutput, status_code=status.HTTP_201_CREATED)
def add_expenses(exp:Expenses):
    print('called Expense obj')
    added_expense = add_expense(exp)
    print("Added Expense:", added_expense)
    return exp


@app.get("/tasks/{task_id}")
def get_expense_based_on_id(task_id:int):
    tasks = list_expenses()
    for item in tasks:
        if item['id'] == task_id:
            return item
    raise HTTPException(status_code=404,detail=f"task_id {task_id} not found")
    

@app.get('/tasks',status_code=status.HTTP_200_OK)
def get_expenses(category:Optional[str] = None, priority: Optional[str] = None):
    expenses = list_expenses()

    if category is not None:
        expenses = [t for t in expenses if t["category"] == category]
    if priority is not None:
        expenses = [t for t in expenses if t["priority"] == priority]
    return expenses

@app.put('/tasks/{task_id}')
def updateExp(task_id:int, exp:Expenses):
    expenses = list_expenses()
    found = None
    for item in expenses:
      if item.get("id") == task_id:
            item.update(exp.model_dump(mode="json"))
            save_expenses(expenses)
            return item
    else:
        return {"Messgage":"Not found"}
    
