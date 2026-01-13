str_1=input("Enter your first string: ")
str_2=input("Enter your second string: ")
if str_1==str_2:
    print ("The strings are equal")
else:
    print ("The strings are not equal")
if len(str_1)>len(str_2):
    print("length of string one is greater than length of string two")
elif len(str_1)==len(str_2):
    print("length of string one is equal to length of string two")
else:
    print("length of string one is not longer than length of string two")