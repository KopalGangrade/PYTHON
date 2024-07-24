
# "f  Draw a flowchart for the following series
# 1==49
# 2==48
# 3==47
# .
# .
# .
# 48==2
# 49==1"


# Write a program to multiply two matrices and store the result in a separate matrix.



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
# | 1  3  5 |
# | 2  4  6 |

A=[[1,2],[3,4],[5,6]]
row=len(A)
col=len(A[0])
m= [[0 for _ in range(row)] for _ in range(col)]
i=0
while i<row:
    j=0
    while j<col:
        m[j][i]=A[i][j]
        j=j+1
    i=i+1
print(A)
for i in m:
    print(i)


# row=2
# col=3
# l=[0]*col
# for i in range(col):
#     m=[0]*row
#     l[i]=m
# print(l)












# "Write a program that prompts for a phone number of 10 digits and two dashes, with dashes after the area code and the next
#  three numbers. For example, 017-555-1212 is a legal input."
# "Write a program that rotates the elements of a list so that the elements at the first index moves to the second and element at 
# the second index move to the third and so on. The last element moves at the first index."
# Write a Program to check whether a given matrix is an identity matrix or not.
# Write a Program to find whether the given matrix is diagonal or not.
# Write a Program to find the sum of all diagonal elements of a matrix.
# Write a Program to find the minimum element in the matrix.
# Write a Program to find the position of an element in a 2d array or Matrix.
# "Say you have a list of lists where each value in the inner lists is a one-character string, like this:
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin 
# is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.
# Copy the previous grid value, and write code that uses it to print the image.
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
# "
# "Take the input from the user and print the following pattern according to the input.
# For example for n = 3 print the following pattern  
#         1 2 3
#         8 9 4
#         7 6 5
# For n = 4 print the following pattern
#           1   2    3   4 
#         12 13 14   5
#         11 16 15   6
#         10   9   8   7 
# "