# def average(a,b,c=1):
#     print("The average is ",(a+b+c)/2)

# #average(4,6)
# # average(b=9)

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is: ",sum/len(numbers))
    # return 7
    return sum/len(numbers)

c=average(5,6,7,1)
print(c)

# def name(fname, mname="Parth", lname="Panchal"):
#     print("Hello,",fname,mname,lname)
# name("Antra","Deepak","Sharma")

def name(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(mname="Kanaiya", lname="Panchal", fname="Parth")