class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} barks"

a1=Animal("chintu")
d1=Dog("mikku")
print(a1.speak())
print(d1.speak())

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
class Manager(Employee):
    def __init__(self,name,salary,teamsize):
        super().__init__(name,salary)
        self.teamsize=teamsize
    def team_info(self):
        return f"{self.name} manages {self.teamsize} people"
e1=Employee("Mikku",2500)
m1=Manager("chintu",1300,4)
print(e1.annual_salary())
print(m1.team_info())
print(m1.annual_salary())
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
c1=Circle(5)
s1=Square(5)
print(c1.area())
print(s1.area())
