import numpy as  np
import json

FILE_NAME = 'Expenses.json'

class Expence_clac:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self,):
        return {
            "Category": self.category,
            "Amount": self.amount,
            "Date": self.date
        }

    def __repr__(self):
        return json.dumps(Expence_clac.to_dict(self)) 


print(Expence_clac("cat", 100, 2-2-2026))
