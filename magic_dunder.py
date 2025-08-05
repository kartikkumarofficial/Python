class Employee:
    name="KK"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name}"
    def __repr__(self):
        return f"The name of the employee is {self.name}"
    def __call__(self):
        print("Hey am good")
e=Employee()
print(e.name)

print(len(e))

# Magic or dunder methods surrounded by double undelescores are tools to customize the behaviour of classes
# used to implement special functions like add ,subtract and more adv things like descriptors and properties



print(str(e))
print(repr(e)) #callback for str , when str not found , this runs

# str and repr are used to represent an object as string representation


# __call__ method is used to make an object callable

e() #will run the __call__ method