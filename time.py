
import time 
time = time.strftime("%H:%M:%S")
if(time>='00:00:00' and time<='12:00:00'):
    print("Good Morning")
elif(time>='12:00:01' and time<='16:00:00'):
    print("Good Afternoon")
elif(time>='16:00:01' and time<='21:00:00'):
    print("Good Evening")
else:
    print("Good Night")
print(time)