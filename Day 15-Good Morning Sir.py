Time=int(input("Enter Time by Hours:"))
if(Time>0 and Time<=12):
    print("Good Morning")
elif(Time>12 and Time<=6):
    print("Good Afternoon18")
else:
    print("Good Evening")

import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp=time.strftime("%H")
print(timestamp)
timestamp=time.strftime("%M")
print(timestamp)
timestamp=time.strftime("%S")
print(timestamp)
