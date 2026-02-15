# Bank Account OOP Project
# Created by Saravanapothi

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")



if __name__ == "__main__":
    account = BankAccount("Saravanapothi", 1000)

    account.deposit(500)
    account.withdraw(300)
    account.withdraw(2000)
