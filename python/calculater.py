print("what do you want to perform")

print("For Add enter 1:")
print("For sub enter 2:")
print("For mul enter 3:")
print("For div enter 4:")

c=int(input("Enter a choice:"))

a=int(input("Enter a number for a:"))
b=int(input("Enter a number for b:"))

if c==1:
    add=a+b
    print("Addition of a and b is:",add)
elif c==2:
    sub=a-b
    print("Substraction of a and b is:",sub)
elif c==3:
    mul=a*b
    print("Multiplication of a and b is:",mul)
elif c==4:
    div=a/b
    print("Division of a and b is:",div)
else:
    print("Wrong choice")






