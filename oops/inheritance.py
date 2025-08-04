class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee {self.id} is {self.name}")

# Employee("Kartik",420).showDetails() #direct way

e1 = Employee("kk",410)
e1.showDetails()


# subclass

class Programmer(Employee):#has all the properties of employee as well as his 
    def showLang(self):
        print("Default language is python")

e2 = Programmer("kk2",34)
e2.showDetails()
e2.showLang()