a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("type 1 for addition ")
print("type 2 for subtraction")
print("type 3 for multiplication ")
print("type 4 for division")
c=int(input("enter 1-4:"))
if (c==1):
    d=a+b
    print("the sum is:",d)
elif (c==2):
    d=a-b
    print("the sub is:",d)
elif (c==3):
    d=a*b
    print("the mul is:",d)
elif (c==4):
    d=a/b
    print("the div is:",d)
else :
    print("invalid option")

print("Thankyou for using calculator")


