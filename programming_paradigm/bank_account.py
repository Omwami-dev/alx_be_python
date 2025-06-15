class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance
    def deposit(self,amount):
        if amount > 0:
            self._account_balance += amount
            raise ValueError
    def withdraw(self,amount):
        #Deduct the specified amount from the account balance if funds are sufficient.
        #Returns True if the transaction is successful, False otherwise.
        self._account_balance = amount
        if amount > self._account_balance:
            return False
        self._account_balance =- amount
        return True
    def display_balance():
        #return curent balance in the account in a friendly manner.
        return f"Current Balance: ${self._account_balance:.2f}"

