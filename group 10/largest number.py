a=float(input("Enter a first number: "))
b=float(input("Enter a second number: "))
c=float(input("Enter a third number: "))

if a>b and a>c:
    print("The largest number is ",a)
elif b>a and b>c:
    print("The largest number is ",b)
elif c>a and c>b:
    print("The largest number is ",c)
else:
    print("all numbers are equal and the number is ",a )
