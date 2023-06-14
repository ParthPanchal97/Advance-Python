for i in range(12):
    print("5 X ",i,"=", 5*(i+1))
    if(i==10):
        break

print("Loop ko chord ke nikal gaya")

for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X ",i,"=", 5*(i+1))
    
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break