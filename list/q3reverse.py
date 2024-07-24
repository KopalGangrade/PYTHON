# Given a list and its size, print the list. in reverse order. (l=[5,4,9,2,1,0])

# l=[5,4,9,2,1,0]
# n=6
# i=n-1
# while i>=0:
#     print(l[i])
#     i=i-1


l=[5,4,9,2,1,0]
i=0
n=6
m=0
while i<n/2:
    m=l[i]
    l[i]=l[n-i-1]
    l[n-i-1]=m
    i=i+1
print(l)




