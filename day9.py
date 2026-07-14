class Book :
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def summary(self):
        return f"{self.title} by {self.author},{self.pages} pages"
B1=Book("my book","asiya",25)
B2=Book("your book","aachu",10)
print(B1.summary())
print(B2.summary())

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
c1=Rectangle(10,2)
print(c1.area())
print(c1.perimeter())

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return"insufficient balance"
        else:
            self.balance-=amount
            return self.balance
ba1=BankAccount("asiya",1000)
ba2=BankAccount("aachu")
print(ba1.deposit(100))
print(ba2.deposit(100))
print(ba1.withdraw(200))
print(ba2.withdraw(400))
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def age(self,current_year):
        return current_year-self.year

C1=Car("bmw",'M',2020)
print(C1.age(2026))
C2=Car("audi","p",1909)
print(C2.age(2026))
