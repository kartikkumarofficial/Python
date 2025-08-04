# # # map function
# # # built in function that allows us to apply a function to sequenceo f data in one go 
# # # map(function , iterable)

# # l=[1,2,3,4,5,6]
# # import math 
# # def cube(num):
# #     return num**3
# # newl = list(map(cube,l))
# # print(l)
# # print(l)


# # filter
# # filters in a seq based on given predicate
# # they take other functions as arg
# l2=[1,2,3,4,5,6,7]
# def greaterthan2(a):
#     return a>2
#     # if(a>2):
#     #     return a
# newl2=list(filter(greaterthan2,l2)) #if true , value will be added 
# print(l2)
# print(newl2)

# # the predicate function is a bool fucntion that returns bool value 



# reduce 
# this functions takes first 2 args from a seq and then performs oepration on it 
from functools import reduce
numbers = [1,2,3,4,5,6,7]
numbers = reduce(lambda x,y : x+y ,numbers)
print(numbers)