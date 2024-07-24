# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# pronic_numbers = []

# num = start
# while num <= end:
#     i = 0
#     while i * (i + 1) <= num:
#         if i * (i + 1) == num:
#             pronic_numbers.append(num)
#         i += 1
#     num += 1

# if pronic_numbers:
#     print("Pronic numbers in the range:", pronic_numbers)
# else:
#     print("No pronic numbers found in the given range.")
# In this code, we use a while loop to iterate through the numbers from start to end. Within the outer while loop, we use another while loop to check if each number is pronic. The pronic numbers found are stored in the pronic_numbers list, and the code prints them at the end.

# text = "I \n am \n kopal gangrade"
# print(text)

# str = "Hello Javatpoint"  
# str2 = str.count('t')  
# print(str2)

str = "ab bc ca de ed ad da ab bc ca"  
oc = str.count('a')  
# Displaying result  
print("occurences:", oc)  