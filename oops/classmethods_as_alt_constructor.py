class Employee:
    # default way
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return(cls(string.split("-")[0],string.split("-")[1]))

    

e = Employee("Kartik",12000)
print(e.name)
print(e.salary)

# what if value is given in some other format like Kartik-12000 then u gotta parse the string 
# not a good way , looks ugly
string = "Kartik-12000"
e1=Employee(string.split("-")[0],int(string.split("-")[1])) #will create ["kartik",12000]
print(e1.name)
print(e1.salary)


print("Using the better way i.e. using class methods as constructor")

# gotta make it better looking using class methods as alternative constructor
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)
