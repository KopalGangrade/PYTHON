
# Write a Program to transpose matrix A. Store the result in a separate matrix.

# A transpose of a matrix is an operation that converts its rows into columns and vice versa. 
# Suppose you have an original matrix A with dimensions m x n, where m represents the number of rows and n
# represents the number of columns. The transpose of matrix A, denoted as A^T, will have dimensions n x m,
# where the number of rows becomes equal to the number of columns and vice versa.
# Original Matrix A (3x2):

# Copy code
# | 1  2 |
# | 3  4 |
# | 5  6 |
# Transpose of A (2x3):

# Copy code
# | 1  3  5 |\

# | 2  4  6 |

# A=[[1,2],[3,4],[5,6]]
# row=len(A)
# col=len(A[0])
# m= [[0 for _ in range(row)] for _ in range(col)]
# i=0
# while i<row:
#     j=0
#     while j<col:
#         m[j][i]=A[i][j]
#         j=j+1
#     i=i+1
# print(A)
# for i in m:
#     print(i)


# s=[[1,2,3],[2,3,4]]
# "h=[[1,2][2,3][3,4]]"
# row=len(s)
# col=len(s[0])
# k=0
# l=[0]*col
# for i in range(col):
#     m=[0]*row
#     l[i]=m
# while k<col:
#     for j in range(row):
#         l[k][j]=s[j][k]
#     k+=1
# print(l)



