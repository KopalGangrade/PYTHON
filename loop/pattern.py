# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print("",end=" ")
#         j=j-1
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k=k+1
#     h=5
#     while h>=i:
#         print("#",end="")
#         h=h-1
    
#     print()
#     i=i+1

# n=int(input("enter a number"))
# m=int(input("enter a number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=m:
#         if i==1 or i==(n//2) or j==1 or i==n:
#             print("*",end=" ")
#         else:
#             print("",end="")
#         j+=1
#     print()
#     i+=1

# n=int(input("enter a number"))
# # m=int(input("enter a number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if i==1 or i==(n-(n//2)) or i==n or j==(n//2):
#             print("*",end="")
#         else:
#             print("",end="")
#         j+=1
#     print()
#     i+=1

# Define the size of the "S" pattern
# size = 5

# # Loop through rows
# for i in range(size):
#     # Loop through columns
#     for j in range(size):
#         if i == 0 or i == size - 1 or i == size // 2:
#             print("*", end="")
#         elif j == 0 and i < size // 2:
#             print("*", end="")
#         elif j == size - 1 and i > size // 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     # Move to the next line after each row
#     print()


m = 10  # Replace with your desired starting value
n = 50  # Replace with your desired ending value

print(f"Prime numbers between {m} and {n}:")
for num in range(m, n + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)


