# Static methods 
# belongs to a class rather than an instance of the class
# defined using the @staticmethod decorator 
# dont have access to the instance of the class

class Math:
    def __init__(self,num):
        self.num= num
    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod #this is static method so no self is req - this object is associated with the class rather than the instance of it
    def add(a,b):
        return a+b
    
    
    # the native non static way is this
    # def add(self,a,b):
    #     return a+b

a=Math(5)
print(a.num)
a=Math(5)
print(a.num)
print(a.add(1,2))