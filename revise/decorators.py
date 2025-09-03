
def greet(fx):
    def wrapper():
        print("good morning")
        fx()
        print("thanx for using this function")
    return wrapper

@greet
def hello():
    print ("hello world")


# @greet
# def add(a,b):
#     return a + b
hello()
