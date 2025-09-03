# numpy is general purpose array processing package 
# creates high performance array object 
import numpy as np

# l=[1,2,3,4,5] 
# arr=np.array(l)
# print(arr)
# print(l)
# print(type(arr))
# print(arr.shape)
# arr.reshape(-1,5)
# print(arr)


l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[11,12,13,14,15]
arr=np.array([l1,l2,l3])
print(arr)
print(arr.shape)
arr=arr.reshape(1,15)
# arr=arr.reshape(-1, 3) numpy finds the first correct dim (-1 is a wildcard dimension in inmup which helps figuring out what dimension should be so the total number of elements are there )
print(arr)
print(arr.shape)


