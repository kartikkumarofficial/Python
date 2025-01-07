#0 1 1 2 3 5
num=int(input("Enter the no. of occurences u wanna see:"))
def fibonacci(n):
    num1=0
    num2=1
    for i in range (n):
        print(num1 , end=' ')  
        sum=num1+num2
        num1=num2
        num2=sum
    
fibonacci(num)


 