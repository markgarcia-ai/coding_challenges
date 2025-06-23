"""
Challenge 17: Encapsulation

Problem Statement:
Create a `BankAccount` class that encapsulates the account balance. The balance should not be directly accessible from outside the class. Instead, access should be controlled through `deposit` and `withdraw` methods.

Requirements:
- Create a class `BankAccount`.
- In the `__init__` method, initialize a "private" attribute for the balance (e.g., `self._balance`). A single underscore is a convention to indicate it's for internal use.
- Create a `deposit(self, amount)` method that adds to the balance. It should not allow depositing a negative amount.
- Create a `withdraw(self, amount)` method that subtracts from the balance. It should not allow withdrawing a negative amount or more than the current balance.
- Create a `get_balance(self)` method to safely retrieve the current balance.

Solution:
"""

class BankAccount:
    """A simple class demonstrating encapsulation for a bank account."""
    def __init__(self, initial_balance=0):
        # The underscore indicates this is a "protected" member for internal use.
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrew: ${amount}")

    def get_balance(self):
        """Safely returns the current balance."""
        return self._balance

# Example usage:
if __name__ == "__main__":
    account = BankAccount(100)
    
    print(f"Initial balance: ${account.get_balance()}")
    
    account.deposit(50)
    account.withdraw(30)
    
    print(f"Final balance: ${account.get_balance()}")
    
    # Try invalid operations
    account.withdraw(200)
    account.deposit(-20)
    
    print(f"Balance after invalid ops: ${account.get_balance()}")
    
    # Direct access is discouraged but possible. Encapsulation is a convention.
    # account._balance = 1000000 
    # print(f"Balance after cheating: ${account.get_balance()}")

"""
Expected Output:

Initial balance: $100
Deposited: $50
Withdrew: $30
Final balance: $120
Insufficient funds.
Deposit amount must be positive.
Balance after invalid ops: $120
""" 