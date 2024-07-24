# n=int(input())
# x=input()
# s=str(input())
# print(n+2)\


# numbers = [1, 3, 4, 2]

# Sorting list of Integers in ascending
# print(numbers.sort())
# print(numbers)

# d = numbers.sort()
# print(d)

# numbers.sort()
# print(numbers)


# n=int(input())
# A=list(map(int,input().split()))
# A.sort()
# for i in range(n):
#   if A[i]!=A[i+1]:
#     print(A[i+1])
#     break


n = int(input())
A = input()
A.sort(reverse=True)
print(A)

for i in range(n - 1):
    if A[i] != A[i + 1]:
        print(A[i + 1])
        break
else:
    print(A[-1])


N = int(input())
A = input()
A = A.split()
for i in range(N):
  A[i] = int(A[i])
first = max(A)
for i in range(N):
  if A[i] == first:
    A[i] = 0
print(max(A))


