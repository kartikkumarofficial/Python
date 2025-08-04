# methods bound to class and not to the instance of class


class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    # normal way , will change company only a instance
    def changeCompany(cls,newCompany):
        cls.company=newCompany

    # class method takes class as first arguement and will make changes in class 
    @classmethod        
    def changeClassCompany(cls,newclasscompany):
        cls.company=newclasscompany

e1=Employee()
e1.name="KK"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print("Instance : ", e1.company)
print("Class    : ",  Employee.company)


print("Now implementing class method")
e1.changeClassCompany("Bajaj")
print("Instance : ", e1.company)
print("Class    : ",  Employee.company)


# when called class to print first checks instance var -> then class var if nothing's there in intance var

