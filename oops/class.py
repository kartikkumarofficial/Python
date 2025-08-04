

class person:
    name = "KK"
    occupation = "Student"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    # self keyword - self parameter is a reference to the current instance of the class , and is used to access variables that belogs to the class 
a = person() #will use values corresponding to a
b = person() #will use values corresponding to b
c = person() #will use default values #creating new object
b.name = "Kartik"
b.occupation = "occupationless"
a = person()
a.name = "Shubhum"

a.info()
b.info()
c.info()
 

print(a.name)


