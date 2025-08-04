# function , if else , recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

# print(factorial(5))

#variable args
def sumall(*all):
    return sum(all)

# print(sumall(333,1))


