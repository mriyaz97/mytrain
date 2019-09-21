
x=int(input("enter a number"))

for i in range (2,x):
    if x%i==0:
        print(x,"not a prime")
        break
    else:
        print(x,"is a prime")
        break
else:
    print(x,"not a prime")










