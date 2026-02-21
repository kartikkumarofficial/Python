# there is no strict public private and protected in python but we still 

# used to limit access of class variables and class methods outside of class , while implementing the concepts of inheritance

# by default everything is public in python

# adding double underscore with make the access limited
class Employee:
    def __init__(self):
        self.__name="KK" #private
        self.normalname="public"
        self._protectedname="protected" #protected

a = Employee()
# print(a.__name) cannot be accessed directly

# public 
print(a.normalname)

# private
print(a._Employee__name) # can be accessed indirectly but can be accessed through name mangling
# print(a._name)cant be accessed like that 

print(a.__dir__())#prints all the methods available in a to run 
 
# protected
# can be only accessed by the member of the class and its subclass 

print(a._protectedname)


