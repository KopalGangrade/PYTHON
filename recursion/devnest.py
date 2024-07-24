# def f():
#     print("start typin....")
#     f()
#     print("end typin....")
# f()

# when we will call function inside body it calls that function again and again.

# def a():
#     print("a1")
#     print('a2')

# def b():
#     print("b1")
#     a()
#     print('b2')


# def c():
#     print("c1")
#     # b()
#     print('c2')
# c()


# def f(n):
#     if n%2==0:
#         print(1)
#     else:
#         print(2)    
# f(10)


# a=[]
# def g():
#     if len(a)==0:
#         print(1)
#         a.append(1)
#         g()
#     else:
#         print(2)
# g()

# print square of numbers
# def f(n):
#     if n==0:
#         return
#     print(n**2)
#     f(n-1)
# f(7)

# change states f1 to f2 , f2 to f3 ..... , fn

# f(1)
# abc
# f(2)
# xyz
# can change by arguments or globAL variable.  

# if number is positive we have to -1


# print factorial numbers

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
result=factorial()
print(result)




