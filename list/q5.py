# Given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘i’ elements of any given list. ‘i’ accepted from the user.

list1= ['a', 1, '2', 5, 'b', 'q']
i=int(input("enter a number"))
n=6
while i<n:
    print(list1[i])
    i=i+1
