l1=[1,2,3,4,5,6,7,8]

for i in range(1,4):
    print(l1[i])
else:
    print("else executed only when loop is executed successfully to its very last value")


for i in range(1,4):
    print(l1[i])
    if(l1[i]==3):
        break
else:
    print("not executed")