# Instance variables = we use them when we wana associate a property to that very object/instance of class
# Class variables = we use them when we wana associate a property a class that all instances share - written at class level
class Employee:
    companyName="Apple"
    def __init__(self,name):
        self.name=name
        self.raiseammount=0.02 #raiseammount is an instance variable here
    
    def showDetails(self):
        print(f"The name of Employee is {self.name} , and ammount raised is {self.raiseammount} in {self.companyName}")
    

emp1=Employee("Kartik")
emp1.companyName="Samsung"
emp1.showDetails()
# Employee.showDetails(emp1) #same

# new instance will use the default class variable unless a new is provided or there is an instance var 
Employee("kk").showDetails()



# if instance variable is there then will use that else look for class variable afterwards
