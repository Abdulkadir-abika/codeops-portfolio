# vehicle hierarchy
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def describe(self):
       print ("This vehicle is",self.make,"with a model of",self.model)
class Car(Vehicle):
    pass
class Truck(Vehicle):
    pass
car1=Car("toyota","vitz")
car1.describe()
# use super()
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def describe(self):
       print ("This vehicle is",self.make,"with a model of",self.model)
class Truck(Vehicle):
    def __init__(self,make,model,capacity):
       super().__init__(make,model)
       self.capacity=capacity
# override
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def describe(self):
       print ("This vehicle is",self.make,"with a model of",self.model)
class Truck(Vehicle):
    def __init__(self,make,model,capacity):
       super().__init__(make,model)
       self.capacity=capacity
    def describe(self):   
        print("This truck is", self.make, self.model, "and has a capacity of", self.capacity, "tons")
#polymorphysm,abstract method
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model    
    def describe(self):
        print("This vehicle is", self.make, "with a model of", self.model)
    @abstractmethod
    def wheels(self):
        pass
class Car(Vehicle):
    def wheels(self):
        return 4
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity
    def describe(self):   
        print("This truck is", self.make, self.model, "and has a capacity of", self.capacity, "tons")
    def wheels(self):
        return 6
car1 = Car("toyota", "vitz")
truck1 = Truck("isuzu", "npr", 5)
car2 = Car("hyundai", "atos")

vehicles_list = [car1, truck1, car2]

for vehicle in vehicles_list:
    vehicle.describe()  
    print("It has", vehicle.wheels(), "wheels.") 
