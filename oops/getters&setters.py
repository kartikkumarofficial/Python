class Myclass:
    def __init__(self,val):
        self.value=val
    # def __init__(self,val2):
    #     self.value2=val2 python doesn't support method overloading natively so here second one will be taken as it overrides the previous one 
        
    def show(self):
        print(f"value is {self.value}")

    @property #decorator to make the fun as property
    def ten_value(self):
        return 10* self.value 
    
    @ten_value.setter #decorator to make setter
    def ten_value(self,new_value):
        self.value = new_value/10

a= Myclass(10)
a.ten_value=67
a.show()