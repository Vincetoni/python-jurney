class specialEvent:
    def __init__(self, event, time, description):
        self.event = input('event: ')
        self.time = input('time: ')
        self.description = input('description: ')

    def to_file_string(self):
        return (
            f"\n🌟 SPECIAL EVENT: {self.event.upper()} 🌟\n"
            f"Date/Time: {self.time}\n"
            f"Description: {self.description}\n"
            "----------------------------------------\n"
        )

    def __repr__(self):
        return self.to_file_string()


entry = specialEvent("", "", "")  
print(entry)                      