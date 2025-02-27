class BankAccount:
    def __init__(self, amount):
        self._amount = amount  

    @property
    def amount(self):
        return self._amount  # Getter for the amount property

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError('Balance cannot go below zero')
        self._amount = value  

    @property
    def withdraw(self):
        """This is a dummy property to allow 'withdraw' to be used as a property."""
        return self._withdraw  # This method will handle the withdrawal logic

    @withdraw.setter
    def withdraw(self, withdrawal_amount):
        """The setter for the 'withdraw' property enforces withdrawal rules."""
        if withdrawal_amount > self._amount:
            raise ValueError("Insufficient funds: Cannot withdraw {}, your balance is {}".format(withdrawal_amount, self.amount))
        if withdrawal_amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        self._amount -= withdrawal_amount  # Deduct the withdrawal amount from the balance


# Example usage
p1 = BankAccount(1000)  # Create an account with 1000 balance
print(f"Initial balance: {p1.amount}")  # Output: Initial balance: 1000

try:
    p1.withdraw = 2000  # Attempt to withdraw 2000 using the property
except ValueError as e:
    print(e)  # Output: Insufficient funds: Cannot withdraw more than the available balance

print(f"Balance after failed withdrawal: {p1.amount}")  # Output: Balance after failed withdrawal: 1000

# Successful withdrawal
p1.withdraw = 500  # Withdraw 500 using the property
print(f"Balance after successful withdrawal: {p1.amount}")  # Output: Balance after successful withdrawal: 500