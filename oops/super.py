# super keyword is useful when class inherits from multiple parent classes and u wanna inherit from one specific parent class 

class ParentCLass:
    def parent_method(self):
        print("This is parent method")

class ChildClass(ParentCLass): #extends ParentClass
    def parent_method(self):
        print("Harry")
        super()
