# method overriding allows us to redefine a method in a derived class 

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
        super().area()
rec = Shape(3,5)
print( "Area of rectangle: ",rec.area())

c=Circle(5)
print( "Area of circle",c.area())
    