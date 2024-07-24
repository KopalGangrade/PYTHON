#1 1. Write a C function that takes three numbers as arguments and returns  the maximum.

def maximum_value(a,b,c):
    if a>b:
        max=a
        smax=b
    else:
        max=b 
        smax=a 
    if c>max:
        print(c)
    else:
        print(max)

# maximum_value(2,6,4)    


# 2. Write a C function that returns the sum of all the elements in an array.
# Sample array : [8, 2, 3, 0, 7]

def arr(m):
    sum=0
    for i in m:
        sum=sum+i
    return sum
# print(arr([8, 2, 3, 0, 7]))


# Expected Output : 20
# 3. Write a C function to check whether a number falls in a given range. Function arguments are
#  (u, l, n) where u=upper limit, l = lower limit and n = number to search for.

def number(u, l, n):
    if n<=u and n>=l:
        return True
    else:
        return False

# print(number(6,3,4)) .
  

# 4. Write a  function to print the even numbers from a given array.
# Sample Array: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]  

def even(m):
    i=0
    p=[]
    for i in m:
        if i%2==0:
            p=p+[i]
    return p
dk=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(even(dk))


# 5. Write a  function that returns the factorial of a number (a non-negative integer).
#  The function accepts the number as an argument.

def factorial(n):
    fac=1
    for i in range (1,n+1):
        fac=fac*i
    return fac
# print(factorial(5))

# 6. Write a  function that takes a number as a parameter and checks whether the number is prime or not. 
# Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
#  other than 1 and itself.

def isprime(n):
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return False
        return True

# print(isprime(9))


# 7. Write a C function to check whether a number is perfect or not.

def perfect(n):
    sum=1
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            sum=sum+(i+(n//i))
    if sum==n:
        return True
    return False 
# num=int(input())
# print(perfect(num))


# 8. Write a C  function that returns the  reverse of a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse(n):
    b=""
    for i in (n):
        b=i+b
    return b
# print(reverse("1234abcd"))




# 9. Write a C function that accepts a string and calculates the number of uppercase letters and lowercase letters.
# Sample String: 'The Quick Brown Fox Jumps Over The Lazy Dog.’'
# Expected Output :
# No. of uppercase characters: 9
# No. of lowercase characters: 26

def cal(string12):
    lower=0
    upper=0
    for i in string12:
        if i>="a" and i<="z":
            lower+=1
        elif i>="A" and i<="z":
            upper+=1
    return(lower,upper)
# print(cal("'The Quick Brown Fox Jumps Over The Lazy Dog.  "))



# 10. Write a C function that takes an array and returns a new array with unique elements of the first array.
# Sample array: [1,2,3,3,3,3,4,5]
# Unique array: [1, 2, 3, 4, 5]

def unique1(n):
    a = []
    for i in range(len(n)):
        if n[i] not in a:
            a += [n[i]]
    return a

# print(unique1([1, 2, 3, 3, 3, 3, 4, 5]))

def uni(a):
    b=[0]*(max(a)+1)
    for i in a:
        b[i]+=1
    for i in range(max(a)+1):
        if b[i]>=1:
            print(i,end=" ")
# uni([1, 2, 3, 3, 3, 7, 4, 5,3])




# 11. Write a  function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., “madam” or “nursesrun”.

def palindrome(pal):
    d=" "
    for i in pal:
        d=i+d
    return d
    if pal==d:
        print("palindrome")
    else:
        print("not palindrome")
# print(palindrome("madaml"))    


def pell(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True
# print(pell("omo"))



# 12. Write a C function to check whether a string is a pangram or not.

def pangram(string):
    b="abcdefghijklmnopqrstuvwxyz"
    for i in b:
        if i not in string.lower():
            return False
    return True
# print(pangram("qazxswedcvfrtgbnhyujmkiossooooooss"))


# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example: "The quick brown fox jumps over the lazy dog"

# 13. Write a C function that prints out the first n rows of Pascal's triangle. Pass n as a function argument.
# Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
# Sample Pascal's triangle :



# Each number is the two numbers above it added together


# 14. Write a  program to access a function inside a function.

# def number(num1,num2):
    
#     print(a+b)
#     number(num+1)
# number(5,7)