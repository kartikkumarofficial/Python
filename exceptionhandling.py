

# when program haults or gives out an error we handle it with try except block


try:
    num = int(input("Enter number: "))
    print(num)

except Exception as e :
    print(e)
except IndexError:
    print("Index Error")
finally:
    print("finally executes always irrespective of the fact whether there's an error or not")
#used to define cleanunp actions that must run no matter what 
# can have multiple excepts in a try except block 
print("rest of the code ")



# custom errors

a = int(input("Enter number between 5 and 9: "))
if ( a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")



# #assesment - to make prog such that if written quit the program will end , and if written any other string , the program will raise a custom error    

try:
    n= input("Enter number between 5 and 9 or type quit: ")
    if(n=="quit"):
        exit()
    if(n.isdigit()==False):
        raise TypeError("The value should be int")
    if (int(n)<5 or int(n)>9):
        raise ValueError("The value should be in between 5 and 9")
   
    print("all good , the value is right")
except Exception as e:
    print(e)