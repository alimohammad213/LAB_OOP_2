class BankAccount:
    def __init__(self, account_holder: str, initial_balance=0):
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance

    def financial(self) -> str:
        return f"BankAccount - Account_holder = {self.__account_holder}, balance = {self.__initial_balance}"
    
    def deposit(self, amount: float) -> float:
        self.__initial_balance += amount
        return self.__initial_balance
    
    def withdraw(self, amount: float):
        if amount > self.__initial_balance:
            raise Exception("Not enough balance")
        self.__initial_balance -= amount
        return self.__initial_balance

    def get_initial_balance(self) -> float:
        return self.__initial_balance
    
    def get_account_holder(self) -> str:
        return self.__account_holder

    def display_balance(self) -> str:
        return f"Current balance: {self.__initial_balance}"

account = BankAccount("Ali", 1000)
print(account.financial())
account.deposit(500)
print(account.display_balance())
account.withdraw(200)
print(account.display_balance())






   
        
