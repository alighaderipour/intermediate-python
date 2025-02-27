class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount

account = BankAccount(1000)
print(account.balance)  # ✅ 1000
account.balance = 500   # ✅ Allowed
# account.balance = -200  # ❌ Error: Cannot set negative balance
