u=int (input("Enter the units consumed \n"))

if u<=100:
    bill=u*5
elif u<=300:
    bill=u*7
elif u <=500:
    bill=u*9
else:
    bill=u*11
print("The bill is",bill)
