# i=1
# while i<=9:
#     j=9
#     while j>=1:
#         print(" ",end=" ")
#         j=j-2
#     k=1
#     while k<=i:
#         print(k,end=" ")
#         k=k+2
#     m=i-1
#     while m>=1:
#         print(m,end="")    
#         m=m+1
#     print()
#     i=i+2       


#           1 
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1

# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(" ",end=" ")
#         j=j-1
#     k=1
#     while k<=i:
#         print(k,end=" ")
#         k=k+1
#     m=i-1
#     while m>=1:
#         print(m,end=" ")
#         m=m-1    
#     print()
#     i=i+1


t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n==m:
        print("yes")
    if n>m:
        a=n-1
        b=m+1
        if a==b:
            print("yes")
        else:
            print("no")
    if n<m:
        b=m-1
        a=n+3
        if a==b:
            print("yes")
        else:
            print("no")


