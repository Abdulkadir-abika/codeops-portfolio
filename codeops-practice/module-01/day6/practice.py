#spot the SRP violation
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def build_text(self):
        return f"Report Title: {self.title} \nContent: {self.content}"
class ReportSaver:
    def __init__(self,report_text,filename):
        self.report_text = report_text
        self.filename = filename 
    def save_file(self):
        with open(self.filename, "w") as file:
            file.write(self.report_text)
        print(f"the report is saved to {self.filename} successfully!")

class EmailSender:
    def __init__(self, recipient, subject, body):
        self.recipient=recipient
        self.subject=subject
        self.body=body
    def send(self):
        print(f"Sending email to {self.recipient}")
        print(f"Subject: {self.subject} {self.body}")

my_report = Report("Sales Report", "We made $1,000 today!")
my_content = my_report.build_text()
print(my_content)

saver = ReportSaver(my_content, "sales_report.txt")
saver.save_file()

email_sender = EmailSender("salesteam@example.com",my_report.title,my_content)
email_sender.send()

#Refactor to OCP
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,shape_type):
        self.shape_type= shape_type
    @abstractmethod
    def shape_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__("rectangle")
        self.width=width
        self.height=height
    def shape_area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self,base,height):
        super().__init__("triangle")
        self.base=base
        self.height=height
    def shape_area(self):
        return self.base * self.height /2

recttange = Rectangle(10, 5)
triangle = Triangle(10, 5)
print(recttange.shape_area())  
print(triangle.shape_area())

#write a singleton

class App_setting:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.currency="ETB"
        return cls._instance
setting1=App_setting()
setting2=App_setting()
print(setting1 is setting2) 

# write a factory
from abc import ABC, abstractmethod

class Circle:
    def draw(self):
        return "Circle is drawing"
class Square:
    def draw(self):
        return "Square is drawing"
class Triangle:
    def draw(self):
        return "Triangle is drawing"
class ShapeFactory:
    @staticmethod 
    def create(kind):
        if kind == "square":
            return Square()  
        elif kind == "circle":
            return Circle()  
        elif kind == "triangle":
            return Triangle()  
        else:
            raise ValueError(f"This '{kind}' type is unknown")
        
shape = ShapeFactory.create("circle")
print(shape.draw()) 

# write an observer pair
class NewsAgency:
    def __init__(self):
        self.subscribers=[]
    def subscribe(self,subscriber):
        self.subscribers.append(subscriber)
    def notify(self,news):
        for subscriber in self.subscribers:
            subscriber.update(news)
class Newspaper:
    def update(self,news):
        print(f"Newspaper received news: {news}")
class TVChannel:
    def update(self,news):
        print(f"TV Channel received news: {news}")

agency= NewsAgency()
newspaper=Newspaper()
tv_channel=TVChannel()
agency.subscribe(newspaper)
agency.subscribe(tv_channel)

agency.notify("Breaking News: New Python course is teaching in IBT!")