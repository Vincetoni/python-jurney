import os
import datetime 
import questionary

FILE_NAME = "journal.txt"

def load_journal():
    """Loads the entire journal as a clean string. Returns empty string if missing."""
    if not os.path.exists(FILE_NAME):
        return ""
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return file.read()  
    
def write_journal():
    """Appends a new multi-line entry to the journal file."""
    entry_lines = [] 
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    print(f"\n--- New Entry Started at {timestamp} ---")
    print("Start typing (Type 'SAVE' on a new line to finish):")
    
    while True:
        line = input(":")
        if line == "SAVE":
            break
        entry_lines.append(line)

   
    with open(FILE_NAME, 'a', encoding='utf-8') as file:
        file.write(f"\n[{timestamp}]\n")
        file.write("\n".join(entry_lines))
        file.write("\n----------------------------------------\n")
        
    print("🎉 Entry saved successfully!")

def show_journal():
    """Displays the current journal content."""
    journal_content = load_journal()
    if not journal_content.strip():
        print('\n🫙 Oops, your journal is empty!')
        return
        
    print("\n================ YOUR JOURNAL ================")
    print(journal_content)
    print("=================================================")

def specialevent():
    class specialEvent:
        def __init__(self, event, time, description):
            self.event = event
            self.time = time
            self.description = description

        def to_file_string(self):
            return (
                f"\n🌟 SPECIAL EVENT: {self.event.upper()} 🌟\n"
                f"Date/Time: {self.time}\n"
                f"Description: {self.description}\n"
                "----------------------------------------\n"
            )

        def __repr__(self):
            return self.to_file_string()

    event = input("Event: ")

    while True:
        time = input("Time (HH:MM): ")

        try:
            datetime.datetime.strptime(time, "%H:%M")
            break
        except ValueError:
            print("❌ Invalid time. Please use HH:MM (e.g. 09:30 or 18:45).")

    description = input("Description: ")

    entry = specialEvent(event, time, description)
    with open(FILE_NAME,'a', encoding='UTF-8') as file:
        file.write(str(entry))
    
def main():
    while True:
        print('\n=== MAIN MENU ===')

        choice = questionary.select(
            "What would you like to do?",
            choices=['Write Journal', 'Show Journal', 'Create Special Journal', 'Close Journal']
        ).ask()
  
        if choice == 'Write Journal':
            write_journal()
        elif choice == 'Show Journal':
            show_journal()
        elif choice == 'Create Special Journal':
            specialevent()
        elif choice == 'Close Journal':
            print('\nClosing journal. Goodbye! 👋')
            break

if __name__ == "__main__":
    main()