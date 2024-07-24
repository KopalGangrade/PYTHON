# Write a program to subtract two matrices and store them in a separate matrix.


a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[2,5,7],[1,3,9],[4,8,6]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        a[i][j]=a[i][j]-b[i][j]
        j=j+1
    i=i+1
print(a)