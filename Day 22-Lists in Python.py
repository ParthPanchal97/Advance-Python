marks=[3,5,6,"Parth",True,6,7,2,32,245,23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #Negative index
print(marks[len(marks)-3]) #Positive index
print(marks[5-3]) #Positive index
print(marks[2]) #Positive index

if "Parth" in marks:
    print("Yes")
else:
    print("No")

#Same thing applies for the strings as well!
if "Pa" in "Parth":
    print("Yes")
else:
    print("No")
    
print(marks[0:len(marks)])
print(marks[1:9])
print(marks[1:9:3])

lst=[i for i in range(10)]
print(lst)
lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]
print(lst)
