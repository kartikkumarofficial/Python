# decorators
# allows u to modify the behaviour of functions and methods
# they are a way to extend the functionlity of a function or method without modifying its source code
# takes another function as an arguement and returns a new function that modifies the behaviour of the original function. 
# the new function is often referred as decorated function 


def greet(fx):
    def mfx():
        print("Good morning") 
        fx() 
        print("Thanks for using this function")
    return mfx    

@greet
def hello():
    print("Hello world")
# greet(hello )() another way
hello()



# for arguements

def mathss(fx):
    def mfx(*args , **kwargs):
        print("good morning again")
        fx(*args,**kwargs)
        print("post function")
    return mfx

@mathss
def add(a,b):
    print(a+b)

add(5,10)