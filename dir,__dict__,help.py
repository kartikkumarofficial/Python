# dir() returns list of all available attributes and methods (including dundet methods -> __methodname__ ) available for an object.
# useful to know what all we can do with the objct

x=[1,2,3,4]

print(dir(x))

# will print what the specific thing is 
print(x.__add__)

y=(1,2,3)
print(dir(y))



class Person:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
p=Person("Kartik",18,15000)
# __dict__ returns dictionary representation of an object's attributes
print(p.__dict__)


print(help(Person))