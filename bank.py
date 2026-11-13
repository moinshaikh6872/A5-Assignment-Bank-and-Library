class Bank:
    def __init__(self, initial_balance=0):
        # Stores balance in a private-style attribute
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        # Refuses an amount above the balance
        if amount > self.__balance:
            print("Withdrawal refused: Insufficient funds.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")

    def get_balance(self):
        # Returns the current balance
        return self.__balance

# Example usage:
# my_account = Bank(100)
# my_account.deposit(50)
# my_account.withdraw(200)
# print(my_account.get_balance())
