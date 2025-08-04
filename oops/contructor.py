
class person:
    def __init__(self,n,o): #dunder method to crate a constructor
        print("Hey I am a person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Kartik", "Student")
b = person("Divya","HR")
a.info()
b.info() 