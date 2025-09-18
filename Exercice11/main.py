class BankAccount:
    def __init__(self, account_holder="", balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount=0.0):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount=0.0):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance !")

    def display_balance(self):
        print("Account holder: ", self.account_holder)
        print(f"Balance: {self.balance}")


bank_account = BankAccount("Toto", 2000.0)
bank_account.display_balance()
bank_account.deposit(500.0)
bank_account.withdraw(3000.0)
bank_account.withdraw(800.0)
bank_account.display_balance()
