# Write a program to create a list of natural numbers till 20 and print it

n=int(input("Enter a number:"))
i=0
a=1
l=[0]*n
while i<n:
    l[i]=a
    a+=1
    i=i+1
print(l)    
