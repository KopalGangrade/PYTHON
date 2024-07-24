# Write a Program to find the minimum element in the matrix.

# note -->how to access all elementsfrom the matrix(nasted array)

# 1] using for loop iteration
# a = [[2, 1, 8], [4, 3, 9], [5, 7, 6]]
# for i in a:
#     for j in i:
#         print(j, end=" ")


# 2]list comprehensions to access all elements in a flat list:

# all_elements = [element for sublist in nested_list for element in sublist]
# print(all_elements)


# 3] using while loop
# a = [[2, 1, 8], [4, 3, 9], [5, 7, 6]]
# i = 0
# l = " "
# while i < len(a):
#     j = 0
#     while j < len(a):
#         print(a[i][j],end=" ")
#         j = j + 1
#     i = i + 1


# 4] Using itertools.chain.from_iterable()
# from itertools import chain

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Using itertools.chain.from_iterable()
# all_elements = list(chain.from_iterable(nested_list))
# print(all_elements)

# 5] using functions
# def print_nested_list(lst):
#     for item in lst:
#         if isinstance(item, list):
#             print_nested_list(item)
#         else:
#             print(item)




# a=[[2,1,8],[4,3,9],[5,7,6]]
# i=0
# while i<=len(a):
#     j=0
#     min=0
#     while j<=len(a[i]):
#         if a[i][j]<a[i+1][j]
#             min=a[i][j]
#         j=j+1
#     i=i+1
# print(min(min))



