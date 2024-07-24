# decimal to binary conversion.
n=int(input("enter a number"))
while n>0:
    if n%2==0:
        print(0,end="")
        n=n//2
    else:
        print(1,end="")
        n=n//2