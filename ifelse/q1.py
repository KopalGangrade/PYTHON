# code of calculator
# n1=int(input("Enter a Number"))
# n2=int(input("Enter a Number"))
# o=input("Enter a Number")
# if (o=="+"):
#     print(n1+n2)
# elif(o == "-"):
#     print(n1-n2)
# elif (o=="*"):
#     print(n1*n2)
# elif(o == "/"):
#     print(n1/n2)
# else:
#     print("no")


# Armstrong code

# n = int(input("Enter a Number"))
# m = n
# sum = 0
# s=len(str(n))
# while n > 0:
#     c = n % 10
#     sum = sum + (c**s)
#     n = n // 10
# if sum == m:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

# Armstrong Number
# n = int(input("Enter a Number"))
# m=n
# count=0
# sum=0
# while n>0:
#     t=n%10
#     count+=1
#     n=n//10
# p=m
# while m>0:
#     d=m%10
#     sum=sum+(d**count)
#     m=m//10
# if sum==p:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

# important
# n = int(input("Enter a Number"))
# m = n
# count = 0
# sum = 0
# while n > 0:
#     count += 1
#     n = n // 10
# p = m
# while m > 0:
#     sum = sum + ((m % 10) ** count)
#     m = m // 10
# if sum == p:
#     print("Yes")
# else:
#     print("No")

# Sum of Elements of a List

# l=[1, 2, 3, 4]
# l=[0,3,-1,2]
# i=0
# sum=0
# b=len(l)
# while i<b:
#   sum=sum+l[i]
#   i=i+1
# print(sum)

# n=int(input("Enter a Number:"))
# l=[0]*n
# i=0
# sum=0
# while i<n:
#     m=int(input("Enter a Number "))
#     l[i]=m
#     i=i+1
#     sum=sum+m
# print(sum)

# s=(input("enter letter:"))
# i=0
# result=0
# b=s.lower()
# while i<len(b):
#     j=i+1
#     c=0
#     while j<len(b):
#         if b[i]>'a' and b[i]<'z':
#             if b[i]==b[j]:
#                 c=c+1
#             j=j+1
#     if c>1:
#         result+=1
#     i=i+1
# if result < 1:
#     print("isogram")
# else:
#     print("not isogram")

# b = input("enter the string:- ")
# a = b.lower()
# i = 0
# c = 0
# while i < len(a):
#     j = 0
#     while j < len(a):
#         if a[i] == a[j]:
#             c = c + 1
#         j = j + 1
#     i = i + 1
# if c < len(a):
#     print("isogram")
# else:
#     print("not isogram")


# b = input("enter the string:- ")
# a = b.lower()
# i = 0
# c = 0
# while i < len(a):
#     j = 0
#     while j < len(a):
#         if a[i] == a[j]:
#             c = c + 1
#         j = j + 1
#     i = i + 1
# if c < len(a):
#     print("isogram")
# else:
#     print("not isogram")


# word = input("Enter a word: ").lower()
# is_isogram = True

# for i in range(len(word)):
#     for j in range(i + 1, len(word)):
#         if word[i].isalpha() and word[i] == word[j]:
#             is_isogram = False
#             break

# if is_isogram:
#     print("The word is an isogram.")
# else:
#     print("The word is not an isogram.")


# alphabet ="abcdefghijklmnopqrstuvwxyz"
# word = str(input(": \n"))
# flag = 0

# for i in alphabet:
#     if i not in word:
#         flag = 1

# if(flag==0):
#     print("It is a pangram")
# else:
#     print("It is not a pangram")


# v = "abcdefghijklmnopqrstuvwxyz"
# word = input(": \n")
# d=word.lower()
# flag = 0
# i = 0

# while i < len(v):
#     if v[i] not in word:
#         flag = 1
#     i += 1

# if flag == 0:
#     print("It is a pangram")
# else:
#     print("It is not a pangram")


# b = input("enter the string:- ")
# a = b.lower()
# i = 0
# c = 0
# while i < len(a):
#     j = 0
#     while j < len(a):
#         if a[i] == a[j]:
#             c = c + 1
#         j = j + 1
#     i = i + 1
# if c > len(a):
#     print("isogram")
# else:
#     print("not isogram")


# a=input("entr a number")
# b='abcdefghijklmnopqrstuvwxyz'
# for i in b:
#    if(i not in a):
#      flag=0
#    else:
#      flag=1
# if(flag==1):
#   print ("pangram")
# else:
#   print ("not pangram")


# a=(input("Enter a String"))
# b='abcdefghijklmnopqrstuvwxyz'
# m=b.len()
# c=0
# i=0
# while i<m:
#     if b[i] in a:
#         c=c+1
#     i=i+1 
# if c==b.len():
#     print("pangram")  
# else:
#     print("not pangram")    



# i=0
# n=5
# l=[0]*n
# while i<n:
#     a=int(input("enter a number:"))
#     l[i]=a
#     i=i+1
# print(l) 
# i=0
# b=[0]*n
# while i<n:
#     j=i+1
#     while j<n:
#         if l[i]==l[j]:
#             b[i]=l[i]
#         j=j+1
#     i=i+1    
# print(b)      



n=int(input("enter a number:"))
l=[0]*n
i=1
while i<n:
    j=1
    sum=0
    while j<i:
        if i%j==0:
            sum=sum+j
        j=j+1
    if sum==i:
        l[i]=j
    i=i+1  
print(l)  