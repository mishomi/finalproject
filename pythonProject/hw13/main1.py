class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} completed. Current balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} completed. Current balance is {self.balance}.")
        else:
            print("Insufficient funds.")

account1 = BankAccount("123456", "John Doe", 1000)
account2 = BankAccount("789012", "Jane Smith", 500)

account1.deposit(500)
account2.withdraw(200)
account1.withdraw(2000)
