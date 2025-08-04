a=[12,3,2,3,44,54,54]

# standard way - gives only value
# index = 0
# for i in a:
#     print(i)
#     if(index==3):
#         print("awsm")
#     index+=1

# enumarate gives us value as well as index while iterative over any data type
marks=[1,2,2,2,2,2,1,1,1]
for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("index found")


# can also add start