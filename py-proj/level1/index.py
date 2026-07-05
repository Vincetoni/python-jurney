import json

def square_up_to(n):
      for i in range(1, n + 1):
           yield i ** 2
     
      
for num in square_up_to(10):
   print(num)

# =============================
# excersise 2
# =============================
class SpecialEvent:
    def __init__(self, title, location, year):
        self.title = title
        self.location = location
        self.year = year

entry = SpecialEvent("Solar Eclipse", "Iceland", 2026)

event_dict = vars(entry)

json_string = json.dumps(event_dict)
print(json_string)