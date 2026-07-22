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
    @property
    def balance(self):
        return self._balance
    def subscribe(self,observer:Alertobserver):
        self._observers.append(observer)
    def _notify(self,messeage):
        for observer in self._observers:
            observer.update(messeage)

    def deposit(self, amount):
        if amount <= 0:
            print("Error: deposit ammount must be positive ")
        else:
            self._balance += amount
            msg=("seccesfully deposited", amount, "ETB to", self.owner, "account")
            print(msg)
            self._notify(msg)
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
        elif self._balance < amount:
            msg=("inseficient balance available ")
            print(msg)
            self._notify(msg)
        else:
            self._balance -= amount
            msg=("seccesfully withdrawn ", amount, "ETB from", self.owner, "account")
            print(msg)
            self._notify(msg)
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
        
acc1 = AccountFactory.create("savings", "riham", 2435451, 5000, rate=0.05)
acc2 = AccountFactory.create("current", "chala", 9988771, 500, overdraft=1000)

sms_service = Smsalert("+251912345678")
acc1.subscribe(sms_service)
acc2.subscribe(sms_service)

acc1.add_interest()
acc2.withdraw(1200)

acc1.statement()
acc2.statement()