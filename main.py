from app.expense_tools import (
    add_expense,
    list_expenses,
    get_total_expenses,
    get_expenses_by_category,
    search_anything,
    total_expense_by_month,
    calculate_expense_total,
    new_print_bill
)
import logging
import os
from dotenv import load_dotenv
# added_expense = add_expense(50.0, "Groceries", "Weekly grocery shopping")
# print("Added Expense:", added_expense)

#added_expense = add_expense(20.0, "Transport", "Bus fare")
# print("Added Expense:", added_expense)
# all_expenses = list_expenses() 

# for expense in all_expenses:
#     print(f"Expense: {expense['amount']} - {expense['category']} - {expense['description']} - {expense['date']}")

# total_expenses = get_total_expenses()


# print(f"Total Expenses: {total_expenses}")
#print(f'calling get expense',get_expenses_by_category("ee"))
#print(f'search anything',search_anything("2026-11"))
#print(f'total amount in specfic month is', total_expense_by_month("2026-11"))
#add_expense = add_expense(-20,"egg","daily once")

#print(f'caliculate *args', calculate_expense_total(10,10,10))
#print(f'call print bill',print_bill())

# @new_print_bill
# def print_bill():
#      print("🧾 Receipt: ₹500 for Dinner")

# print_bill()
# Exception
a = 10
b = 2


# try: 
#     print('file opened')
#     print(a/b)
#     k = int(input('enter value '))
#     print('K value is',k)

# except ZeroDivisionError as e:
#     print('Zero Division error',e)
# except Exception as e:
#     print('exception =>',e)
# else:
#         print(f"✅ Success! The answer ")

# finally:
#     print('file closed') #%(asctime)s
logging.basicConfig(level=logging.DEBUG, filename=('log.log'), filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', force=True)

# logging.debug('debug1')
# logging.info('info1')
# logging.warning('Warning1')
# logging.error('Error1')
# x = 5
# y = 0
# try:
#     result = x/y
# except Exception as e:
#     logging.exception(f"An error occurred1: {e}") 

# Custom Logger

logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s- %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("testing in seperate log")
load_dotenv()
mainkey = os.environ.get('MAINKEY')
print(f'mainkey from env',mainkey)
