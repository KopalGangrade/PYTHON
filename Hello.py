# print("Hello World")

# a = input("enter string")
# b = a.lower()
# # print(b)
# i = 0
# while i < len(b):
#     j = i + 1
#     c = 0
#     while j < len(b):
#         if b[i] == b[j]:
#             c = c + 1
#         j = j + 1
#     if c>1:
#         print("not isogram")
#     else:
#         print("isogram")


# i=1
# while i<=7:
#     j=1
#     while j<=i:
#         if i%j==0:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(" ",end=" ")
#         j=j-1
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k=k+1
#     m=i-1
#     while m>=1:
#         print("*",end=" ")
#         m=m-1
#     print()
#     i=i+1


# a1 a2 a3 second max

# a1=int(input("enter a number:"))
# a2=int(input("enter a number:"))
# a3=int(input("enter a number:"))
# b1=int(input("enter a number:"))
# b2=int(input("enter a number:"))
# b3=int(input("enter a number:"))
# if a1>a2:
#     max=a1
#     smax=a2
# else:
#     max=a2
#     smax=a1
# if a3>smax:
#     smax=a3
# else:
#     smax
# A=max+smax
# if b1>b2:
#     max=b1
#     smax=b2
# else:
#     max=b2
#     smax=b1
# if b3>smax:
#     smax=b3
# else:
#     smax
# B=max+smax
# print(A)
# print(B)
# if A>B:
#     print("alice")
# if A==B:
#     print("tie")
# else:
#     print("bob")


# if a1>a2:
#     max=a1
#     smax=a2
# else:
#     max=a2
#     smax=a1
# if a3>smax:
#     smax=a3
# else:
#     smax
# print(max)
# print(smax)

# n=int(input("enter a number"))
# i=2
# while i<=n:
#     j=1
#     while j<=4-i:
#         print(" ",end=" ")
#         j=j+1
#     k=1
#     while k<=i:
#         print("*",end="")
#         k=k+1
#     print()
#     i=i+1


# i=0
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2==0:
#             print(" ",end="")
#         else:
#             print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1


# i=1
# a=1
# while i <= 4:
#     j = 1
#     while j <= i:
#         print(a, end=" ")
#         a = a + 1
#         j = j + 1
#     print()
#     i = i + 1


# # 123   , 3456  , 45667
# n=int(input("enter  a number:"))
# m=n
# sum=0
# c=0
# while n>0:
#     c=c+1
#     n=n//10   
# p=m
# while m>0:
#     s=m%10
#     sum=sum+(s**c)
#     m=m//10
# if sum==p:
#     print("armstrong")
# else:
#     print("not armstrong")       






# Armstrong Number
# n = int(input("Enter a Number"))
# m = n
# count = 0
# sum = 0
# while n > 0:
#     t = n % 10
#     count += 1
#     n = n // 10
# p = m
# while m > 0:
#     d = m % 10
#     sum = sum + (d**count)
#     m = m // 10
# if sum == p:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")




# height = int(input("enter a number"))
# width =  int(input("enter a number"))

# # Loop through each row
# for row in range(height):
#     # Loop through each column
#     for col in range(width):
#         # Print the letter based on the position
#         if (row == 0 or row == height - 1 or row == height // 2) or (col == 0):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     # Move to the next line after each row
#     print()



# n1 = int(input("enter number"))
# n2 = int(input("enter number"))

# i = 0
# while i < n1:
#     j = 0
#     while j < n2:
#         # Print the letter based on the position
#         if (i == 0 or i == n1 - 1 or i == n1 // 2) or (j == 0):
#             print("*", end=" ")
#         else:
#             print(" ", end="")
#         j += 1
    
#     print()
#     i += 1



# l=[1,6,5,9,4]
# i=0
# sum=0
# while i<len(l):
#     sum=sum+l[i]
#     i=i+1
# print(sum)



# armstrong

n=int(input("enter a number"))
m=n
sum=0
c=0
while n>0:
    s=n%10
    c=c+1
    sum=(s**c)
    print(sum)
    n=n//10

# p=m
# while m>0:
#     d=m%10
#     sum=sum+(d**c)
#     m=m//10
# if sum==m:
#     print("arm")
# else:
#     print("not")    


# a=input("enter string") #fjkfjene
# b="abcdefghijklmnopqrstuvwxyz"
# i=0
# c=0
# while i<len(b):
#     if b[i] in a:
#         c=c+1
#     i=i+1
# if c==len(b):
#     print("pangram")
# else:
#     print("not")    






    
