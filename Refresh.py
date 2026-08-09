import numpy as np
from pathlib import Path
import os
import json

FOLDER_NAME = Path("python-jurney")
FILE_NAME = FOLDER_NAME /'Expenses.json'

class Expence_clac:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date
        self.log = []

    def to_dict(self):
        return {
            "Category": self.category,
            "Amount": self.amount,
            "Date": self.date
        }
    def __repr__(self):
        return json.dumps(self.to_dict()) 


def load_expence():
    """Loads the expenses file or creates an empty one with a list if not existing"""
    # 1. If file does NOT exist, create an empty JSON list [] and save it
    if not os.path.exists(FILE_NAME):
        print(f'File does not exist: creating file as -- {FILE_NAME}')
        with open(FILE_NAME, 'w', encoding="UTF-8") as file:
            json.dump([], file)  # Properly formats it as an empty JSON list
        return []
    # 2. If it DOES exist, read the data safely using 'r' mode
    with open(FILE_NAME, 'r', encoding="UTF-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return [] 

def save_expenses():
    """Takes user inputs, converts to dict, reads file, appends, and saves back"""
    # 1. Gather input data
    category = input("Category: ")
    amount = input("Amount: ")
    date = input("Date: ")
    
    # 2. Create object and convert to a clean dictionary
    expense_obj = Expence_clac(category, amount, date)
    expense_dict = expense_obj.to_dict()  
    
    # 3. Read the existing dataset first
    existing_data = load_expence()
    
    # 4. Append the new item to our Python list
    existing_data.append(expense_dict)
    
    # 5. Overwrite the file with the complete, valid JSON list
    with open(FILE_NAME, 'w', encoding='UTF-8') as file:
        json.dump(existing_data, file, indent=4) # indent=4 makes it readable
    print("Expense saved successfully!")




data = load_expence()
save_expenses()
print("Loaded Data:", data)

# Expense class          ← knows about ONE expense 
#   __init__
#   to_dict()
#   __repr__

# standalone functions   ← know about ALL expenses / the app
#   todo:load_expenses()      → reads JSON file, returns a list of Expense objects =done?
#   todo:save_expenses()      → takes the list, writes to JSON file -done?
#   todo:add_expense()        → asks user for input, returns a new Expense
#   todo:show_all()           → loops the list, prints each one via __repr__
#   todo:summary()            → numpy math on the list
#   todo:chart()              → matplotlib bar chart
#   todo:main()               → the menu loop