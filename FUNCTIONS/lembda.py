# single expression

# Lembda Function 

# is small anonymous function without a name.It is defined using the lambda keyword and has the following syntax:

# lambda arguments : expression

# it is used in condition of small function required for a sort period of time.
    
# example 

# def myfunc(n):
#   return lambda a : a * n

def num(x):
    return x*2  
# print(num(5))

num=lambda x : x*2
# print(num(5))

# cube=lambda y : y*y*y
# print(cube(5)) 

sum= lambda  a,b : ( a + b )
# print(sum(4,7))

avg = lambda d,k : (d+k)//2
# print(avg(4,8))

# note -> we can pass function to function as argument.
square= lambda m : m*m
# def app(fn,value):
    # return 6 + fn(value)
    
# print(app(square,2))


def aply(fun,val1,val2):
    return 5 + fun(val1,val2)
# print(aply(lambda s,t : s-t,8,6))






dip=lambda x: x**x
print(dip(5))