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


class AccountRegistry:
    def __init__(self):
        self.accounts = {}

    def add(self, account: AddisBankAccount):
        if account.acc_num in self.accounts:
            raise ValueError(f"Account number {account.acc_num} already exists.")
        self.accounts[account.acc_num] = account

    def find(self, acc_num) -> AddisBankAccount:
        return self.accounts.get(acc_num, None)

    def list_all(self) -> list:
        return list(self.accounts.values())


if __name__ == "__main__":
    registry = AccountRegistry()

    acc1 = AccountFactory.create("savings", "riham", 2435451, 5000, rate=0.05)
    acc2 = AccountFactory.create("current", "abdu", 9988771, 500, overdraft=1000)

    sms_service = Smsalert("+251912345678")
    acc1.subscribe(sms_service)

    registry.add(acc1)
    registry.add(acc2)

    found = registry.find(2435451)
    print(f"[O(1) Find Result] Owner: {found.owner}, Balance: {found.balance} ETB ")

    
    for acc in registry.list_all():
        acc.statement()
    print()

    found.deposit(1000)
    found.withdraw(300)
    print(f"Current Balance: {found.balance} ETB\n")

    found.undo_last()
    print(f"Balance after 1st undo: {found.balance} ETB")

    found.undo_last()
    print(f"Balance after 2nd undo: {found.balance} ETB")