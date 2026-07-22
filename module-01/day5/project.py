class AddisBankAccount:
    def __init__(self, Owner, acc_num, balance):
        self.owner = Owner
        self.acc_num = acc_num
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Error: deposit ammount must be positive ")
        else:
            self.__balance += amount
            print("seccesfully deposited", amount, "ETB to", self.owner, "account")
            
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
        elif self.__balance < amount:
            print("inseficient balance available ")
        else:
            self.__balance -= amount
            print("seccesfully withdrawn ", amount, "ETB from", self.owner, "account")
            
    def statement(self):
        print(self.owner, ":", self.__balance, "ETB")

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
        if self.balance + self.overdraft >= amount:
            self.deposit(-amount)
            print("seccesfully withdrawn (Overdraft used)", amount, "ETB from", self.owner, "account")
        else:
            print("Error: Overdraft limit exceeded!")
    def statement(self):
        print("[Current Account]", self.owner, ":", self.balance, "ETB (Overdraft:", self.overdraft, "ETB)")
acc1 = AddisBankAccount("abdu", 3345221, 10000)
acc2 = SavingsAccount("riham", 2435451, 5000, 0.05)
acc3 = CurrentAccount("chala", 9988771, 500, 1000)

acc2.add_interest()
acc3.withdraw(1200)
   
accounts_list = [acc1, acc2, acc3]
for account in accounts_list:
    account.statement()