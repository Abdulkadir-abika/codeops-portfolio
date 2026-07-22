class AddisBankAccount:
    def __init__(self,Owner,acc_num,balance):
        self.owner=Owner
        self.acc_num=acc_num
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount <= 0:
            print ("Error: deposit ammount must be positive ")
        else:
            self.__balance+=amount
            print("seccesfully deposited",amount,"ETB to",self.owner,"account")
    def withdraw(self,amount):
        if amount<=0:
            print("Error: Withdrawal amount must be positive!")
        elif self.__balance  < amount:
            print("inseficient balance available ")
        else:
            self.__balance-=amount
            print("seccesfully withdrawn ",amount,"ETB from",self.owner,"account")
    def statement(self):
        print(self.owner,self.__balance, "ETB")
account1=AddisBankAccount("abdu",3345221,10000)
account2=AddisBankAccount("riham",2435451,5000)
account1.statement()
account2.statement()

account1.deposit(300)
account2.deposit(-59)

account1.withdraw(20000)
account2.withdraw(4000)

account1.statement()
account2.statement()