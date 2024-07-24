

# a=10
# print(bin(a).replace("0b"," "))


n=int(input("enter a number"))
l=[0]*n
i=0
while n>0:
    if n%2==0:
        l[i]=0
        i+=1
        n=n//2
    else:
        l[i]=1
        i+=1
        n=n//2
print(l)



        
    