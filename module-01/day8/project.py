from abc import ABC, abstractmethod

class Alertobserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Smsalert(Alertobserver):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, message):
        print(f"SMS sent to {self.phone_number}: {message}")

class AddisBankAccount:
    def __init__(self, Owner, acc_num, balance):
        self.owner = Owner
        self.acc_num = acc_num
        self._balance = balance
        self._observers = []
        self.history_stack = []

    @property
    def balance(self):
        return self._balance

    def subscribe(self, observer: Alertobserver):
        self._observers.append(observer)

    def _notify(self, messeage):
        for observer in self._observers:
            observer.update(messeage)

    def deposit(self, amount):
        if amount <= 0:
            print("Error: deposit ammount must be positive ")
        else:
            self._balance += amount
            self.history_stack.append({"type": "deposit", "amount": amount})
            msg = f"seccesfully deposited {amount} ETB to {self.owner} account"
            print(msg)
            self._notify(msg)

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
        elif self._balance < amount:
            msg = "inseficient balance available "
            print(msg)
            self._notify(msg)
        else:
            self._balance -= amount
            self.history_stack.append({"type": "withdraw", "amount": amount})
            msg = f"seccesfully withdrawn {amount} ETB from {self.owner} account"
            print(msg)
            self._notify(msg)

    def undo_last(self):
        if not self.history_stack:
            print(f"No transactions to undo for {self.owner}.")
            return None

        last_tx = self.history_stack.pop()
        tx_type = last_tx["type"]
        amount = last_tx["amount"]

        if tx_type == "deposit":
            self._balance -= amount
            msg = f"Undo executed: Reversed deposit of {amount} ETB."
        elif tx_type == "withdraw":
            self._balance += amount
            msg = f"Undo executed: Reversed withdrawal of {amount} ETB."

        print(msg)
        self._notify(msg)
        return last_tx

    def total_transactions_recursive(self, history=None):
        if history is None:
            history = self.history_stack
        if not history:
            return 0
        return history[0]["amount"] + self.total_transactions_recursive(history[1:])

    def statement(self):
        print(self.owner, ":", self._balance, "ETB")


class SavingsAccount(AddisBankAccount):
    def __init__(self, Owner, acc_num, balance, rate=0.05):
        super().__init__(Owner, acc_num, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)
        print("Interest of", interest, "ETB added.")

    def statement(self):
        print(self.owner, ":", self.balance, "ETB (Rate:", self.rate, ")")


class CurrentAccount(AddisBankAccount):
    def __init__(self, Owner, acc_num, balance, overdraft=1000):
        super().__init__(Owner, acc_num, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
        elif self.balance + self.overdraft >= amount:
            self._balance -= amount
            self.history_stack.append({"type": "withdraw", "amount": amount})
            msg = f"seccesfully withdrawn (Overdraft used) {amount} ETB from {self.owner} account"
            print(msg)
            self._notify(msg)
        else:
            msg = f"Error: Overdraft limit exceeded for {self.owner}!"
            print(msg)
            self._notify(msg)

    def statement(self):
        print("[Current Account]", self.owner, ":", self.balance, "ETB (Overdraft:", self.overdraft, "ETB)")


class AccountFactory:
    @staticmethod
    def create(kind, Owner, acc_num, balance, **kwargs):
        kind = kind.lower()
        if kind == "savings":
            return SavingsAccount(Owner, acc_num, balance, **kwargs)
        elif kind == "current":
            return CurrentAccount(Owner, acc_num, balance, **kwargs)
        else:
            raise ValueError(f"Unknown account type: '{kind}'")

def binary_search(items, target):
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


class AccountRegistry:
    def __init__(self):
        self.by_number = {}

    def add(self, account: AddisBankAccount):
        if account.acc_num in self.by_number:
            raise ValueError(f"Account number {account.acc_num} already exists.")
        self.by_number[account.acc_num] = account

    def top_by_balance(self, n=5):
        accts = sorted(self.by_number.values(), key=lambda a: a.balance, reverse=True)
        return accts[:n]

    def find_by_number(self, number):
        nums = sorted(self.by_number.keys())
        i = binary_search(nums, number)
        return self.by_number[nums[i]] if i >= 0 else None

    def total_transactions(self, number):
        account = self.find_by_number(number)
        if account:
            return account.total_transactions_recursive()
        return 0
    
registry = AccountRegistry()
acc1 = AccountFactory.create("savings", "riham", 2435451, 5000, rate=0.05)
acc2 = AccountFactory.create("current", "chala", 9988771, 500, overdraft=1000)
acc3 = AccountFactory.create("savings", "abdu", 1122334, 12000, rate=0.05)

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)

for acc in registry.top_by_balance(2):
    acc.statement()
found = registry.find_by_number(2435451)
if found:
    print(f"Found: {found.owner}, Balance: {found.balance} ETB")

found.deposit(1000)
found.withdraw(200)
total_val = registry.total_transactions(2435451)
print(f"Total transaction amount for {found.owner}: {total_val} ETB")