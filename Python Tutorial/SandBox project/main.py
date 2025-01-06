import os

class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = self.generate_account_number()
        
        # Creating the filename for storing transactions
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        
        # Create the file if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write("Transaction History:\n")
                file.write(f"Account Created: {self.accountType} Account for {self.name}\n")
                file.write(f"Initial Balance: {self.balance}\n")
        
    def generate_account_number(self):
        # Generate a random account number (you can implement a more advanced system later)
        return str(hash(self.name + self.accountType))[:10]  # Limiting it to 10 digits

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction(f"Deposited {amount}")
            print(f"Deposited {amount} into the account. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.record_transaction(f"Withdrew {amount}")
            print(f"Withdrew {amount} from the account. New Balance: {self.balance}")
    
    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.accountNumber
    
    def get_username(self):
        return self.name
    
    def get_account_type(self):
        return self.accountType
    
    def record_transaction(self, transaction_detail):
        with open(self.filename, 'a') as file:
            file.write(f"{transaction_detail}: Balance is now {self.balance}\n")
    
    def get_transaction_history(self):
        with open(self.filename, 'r') as file:
            return file.read()

# Testing the BankAccount class with various transactions
if __name__ == "__main__":
    # Create new accounts
    account1 = BankAccount("Alice", "Chequing")
    account2 = BankAccount("Bob", "Savings")
    
    # Perform some transactions
    account1.deposit(1000)
    account1.withdraw(500)
    account1.deposit(200)
    
    account2.deposit(2000)
    account2.withdraw(1500)
    
    # Check account details
    print(f"Account 1 Balance: {account1.get_balance()}")
    print(f"Account 2 Balance: {account2.get_balance()}")
    
    # Display transaction history for each account
    print("\nTransaction History for Account 1:")
    print(account1.get_transaction_history())
    
    print("\nTransaction History for Account 2:")
    print(account2.get_transaction_history())
    
    # Retrieve account details
    print(f"Account 1 ID: {account1.get_account_number()}")
    print(f"Account 1 Username: {account1.get_username()}")
    print(f"Account 1 Type: {account1.get_account_type()}")
