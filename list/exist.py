 # Given a list ([1,2,3,4,5,6,7]), take a number from the user and check whether it exists in the list or not

# m=[1,2,3,4,5,6,7]
# i=0
# n=7
# j=int(input("enter a number:"))
# while i<n:
#     if m[i]==n:
#         print("exist")
#     else:
#         print("not exist")
#     i=i+1


# Write a program to create a list of 7 numbers from the user, and print true if the complete list consists of consecutive numbers or not.

# k=[3,2,4,7,8,1,2]
# i=0
# t=l[i+1]-l[i]
# while i<k:
#     if t==1:
#         print("true")
#     else:
#         print("false")
#     i=i+1    

# Make a flowchart to find the sum and average of elements in a list. Take elements as input from the user.
# Make a flowchart to count the total occurrences of a number in the list. Input the numbers from the user.

# m=[3,5,8,3,8,5,4]
# n=int(input("enter a number:"))
# i=0
# s=7
# c=0
# while i<s:
#     if m[i]==n:
#         c=c+1
#     i=i+1
# print(c)    



# Make a flowchart to count positive and negative elements in a list. Take elements as input from the user.
# Make a flowchart to print duplicates in a list.
# Create a list that stores first n even numbers. Take n as input from the user.

# n=int(input("enter a number:"))
# l=[0]*n
# i=0
# a=1
# while i<n:
#     if a%2==0:
#         l[i]=a
#     a=a+1
#     i=i+1
#     print(l)    


# Create a list that stores first n odd numbers. Take n as input from the user.


# Create a list that stores all the factors of a number n. Take n as input from the user.

# n=int(input("enter a number:"))
# l=[0]*n
# i=1
# a=0
# while i<=n:
#     if n%i==0:
#         l[a]=i
#     i=i+1
#     a=a+1
# print(l)


# Create a list that stores all the prime numbers up to n. Take n as input from the user.

# n=int(input("enter a number"))
# l=[0]*n
# i=1
# m=0
# while i<=n:
#     j=1
#     c=0
#     while j<=n:
#         if (i%j==0):
#             c=c+1
#         j=j+1
#     if c==2:
#         l[m]=i
#         m=m+1
#     i=i+1
# print(l)
     
# Create a list that stores perfect numbers up to n. Take n as input from the user.

# n=int(input("enter a number:"))
# l=[0]*n
# i=1
# while i<n:
#     j=1
#     sum=0
#     while j<i:
#         if i%j==0:
#             sum=sum+j
#         j=j+1
#     if sum==i:
#         print(i)
#         l[i]=j
#     i=i+1
# print(l)

# Create a list that stores Armstrong numbers up to n. Take n as input from the user.
# Create a list that stores the factorial of first n natural numbers. Take n as input from the user.
# Write a program to create a list of 10 numbers from the user, and count the number of odd and even numbers.
# Write a program to create a list of 10 numbers from the user,  and sum the elements on odd positions as odds and on even positions as evens.
# Construct a flowchart to create a list of n items where n is input from the user. Then input n names from the user and add them to the list.
# In the flowchart of the above question, print the names input by the user in reverse order.
# Construct a flowchart to show how to rearrange the elements in an array so that they appear in reverse order.
# Construct a flowchart to input n numbers from the user. Store them in a list, Then show how to determine the maximum number.
# Construct a flowchart to show how to store the first 100 natural numbers in an array and then show them in the reverse sequence.
# In a certain hospital, the weights of newborn babies are recorded each month and then processed at the end of the month to determine the following:
# mean weight of the babies
# maximum of the weights
# minimum the weights
# Construct a flowchart to show how the weights can be stored as a list first and then processed to determine the desired outputs. Input n from the user where n is number of babies born in a particular month.
# In a certain city, the maximum and the minimum temperatures on each day are recorded each month to determine the following at the end of the month:
# mean maximum temperature in the month
# mean minimum temperature in the month
# highest maximum temperature
# lowest minimum temperature
# hottest day number of the month
# coldest day number of the month
# Draw a flowchart to show how the desired result can be obtained. Input n from the user where n is number of days.
# Three tests are given, each one worth 50 points. The better score of the first two tests is added to that of the third one to determine the final score and a grade is assigned to each student on the percentage score as per the following rules.
# Percentage in Score Grade
# > = 80 				A
# > = 70 but <80 		B
# > = 60 but <70 		C
# > = 50 but <60 		D
# < 50 				F
# Develop a flowchart to show how to accept the input data related to each student and process them to print out a result sheet with the output in descending order of the percentage score.
# Draw a flowchart to obtain the sum and the difference between two matrices.



n=int(input("enter the number"))
l=[0]*n
m=0
i=1
while i<=n:
    j=1
    c=0
    while j<=n:
        if i%j==0:
            c+=1
        j=j+1
    if c==2:
        l[m]=i
        m=m+1
    i=i+1  
print(l)          
