

# a=10
# print(bin(a).replace("0b"," "))


# a=int(input("enter a number"))



l=[[1,4,7],[2,5,8],[3,6,9]]
j=0
i=0
s1=0
s2=0
while i<len(l):
    s1+=l[i][j]
    i+=1
    j+=1
i1=0
j1=len(l)-1
while i1<len(l):
    s2+=l[i1][j1]
    i1+=1
    j1-=1
print(s1,s2)