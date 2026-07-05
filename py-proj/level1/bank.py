class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = int(balance)
        self.history = []

    def deposit(self, amount):
        amount = int(amount)
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: ${amount}")
            return f"Deposited: ${amount}"
        else:
            return "Invalid amount: must be more than 0"
    
    def withdraw(self, amount):
        amount = int(amount)
        if amount <= 0:
            return "Invalid amount: must be more than 0"
        elif amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew: ${amount}")
            return f"Withdrew: ${amount}"
        else:
            return "Insufficient funds"
        
    def transfer(self, amount, other_acct):
         amount = int(amount)
         if amount <= 0:
             return "Invalid transfer amount"
         if amount <= self.balance:
             self.balance -= amount                                    
             other_acct.balance += amount                                 
             self.history.append(f"Transferred ${amount} to {other_acct.owner}")
             other_acct.history.append(f"Received ${amount} from {self.owner}")
             return f"Transferred ${amount} to {other_acct.owner}"
         else:
             return "Transfer failed: Insufficient funds"    

    def __repr__(self):
        return f"BankAccount(Owner: '{self.owner}', Balance: ${self.balance})"

# ==========================================
# DRIVER SCRIPT (Testing our code)
# ==========================================

vincent = BankAccount('Vincent', 1000)
kat = BankAccount('Kat', 10)

print("--- Initial State ---")
print(vincent)
print(kat)

print("\n--- Running Transactions ---")
vincent.deposit(500)
vincent.withdraw(200)
vincent.transfer(300, kat)  

print("\n--- Final State ---")
print(vincent)
print(kat)

print("\n--- Vincent's History ---")
print(vincent.history)

print("\n--- Kat's History ---")
print(kat.history)