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

def create_special_journal():

    date_format = "%Y-%m-%d %H:%M"

    sepcial_journal = {
        'event': '',
        'time': '',
        'description' : ''
    }

    sepcial_journal['event'] = input('event:')
    sepcial_journal['description'] = input('describe your event:')
    sepcial_journal['time'] = input("Enter date and time (YYYY-MM-DD HH:MM): ")  

    try:
     user_datetime = datetime.datetime.strptime(sepcial_journal['time'], date_format)
     print(f"Success!: {user_datetime}")
     print(f"succesfuly created event for {sepcial_journal['event']} at {user_datetime.year}:{user_datetime.month}")   

     with open (FILE_NAME, 'a', encoding='utf-8') as file:
         with open(FILE_NAME, 'a', encoding='utf-8') as file:
            file.write(f"\n🌟 SPECIAL EVENT: {sepcial_journal['event'].upper()} 🌟\n")
            file.write(f"Date/Time: {sepcial_journal['time']}\n")
            file.write(f"Description: {sepcial_journal['description']}\n")
            file.write("----------------------------------------\n")
            
    except ValueError:

     print("Error: The date format did not match YYYY-MM-DD HH:MM.")


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
            create_special_journal()
        elif choice == 'Close Journal':
            print('\nClosing journal. Goodbye! 👋')
            break

if __name__ == "__main__":
    main()