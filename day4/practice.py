#ex1 Book class
class Book:
    def __init__(self,title,author,page):
        self.title=title
        self.author=author
        self.page=page
    def describe(self):
        print("this",self.title,"book is written by",self.author,"and it have",self.page,"pages")
book1=Book("tlkusew","ustaz seid ahmed",545)
book2=Book("the secret","rhonda byrne",200)
book1.describe()
book2.describe()

#ex2 product class
class Product:
    def __init__(self,name,price,quantity):
        self.name= name
        self.price= price
        self.quantity= quantity
    def restock(self,n):
       self.quantity += n
    def sell(self,n):
        self.quantity -= n
    def statement(self):
        print(self.name  ,self.quantity, "units are available")    
product1=Product("samsung",15000,10)
product1.restock(9)
product1.statement()
product1.sell(5)
product1.statement()


#ex3,ex4,ex5 make it private,validate,prove independence
class Product:
    def __init__(self,name,price,quantity):
        self.name= name
        self.price= price
        self.__quantity= quantity
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print("Error: Quantity cannot be negative!")
        else:
            self.__quantity = value
    def restock(self,n):
       self.__quantity += n
    def sell(self,n):
        if self.__quantity - n < 0:
            print("Error: Not enough stock! Sale cancelled.")
        else:
            self.__quantity -= n
    def statement(self):
        print(self.name  ,self.__quantity, "units are available")
product1=Product("samsung",15000,10)
product2 = Product("apple", 25000, 5)
product3 = Product("sony", 8000, 12)
product1.restock(9)
product1.statement()
print("Current quantity is:", product1.quantity)
product1.sell(20) 

product1.quantity=100
product1.statement()   
product2.statement()
product3.statement()
