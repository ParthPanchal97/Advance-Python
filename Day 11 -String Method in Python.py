#String are immutable
a = "!!!Parth!!! !!!Parth!!! !!!Arjun!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Parth","Arjun"))
print(a.split(" "))

blogHeading="Introduction to Python"
print(blogHeading.capitalize())

str1="Welcome to the Python!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Parth"))
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

str2="He's name is Ryu. He is an honest man."
print(str2.find("is"))
# print(str2.index("ishh"))
print(str2.title())

str3="WelcomeToTheConsole09"
print(str3.isalnum())
str3="Welcome"
print(str3.isalpha())

str4="hello world"
print(str4.islower())

str5="We wish you a Merry Chrishmas\n"
print(str5)
print(str5.isprintable())

str6="      " #using spacebar or tab
print(str6.isspace())

str7="World Health Organization"
print(str7.istitle())

str8="To Kill a Mocking bird"
print(str8.istitle())

str9="Python is a Interpreted Language"
print(str9.startswith("Python"))

str10="Python is a Interpreted Language"
print(str10.swapcase())