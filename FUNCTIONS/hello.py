# reuseablity of code and readablity increases performance   // important

#  function ka defination
# A function is a block of code which only runs when it is called. You can pass data,
#  known as parameters, into a function. A function can return data as a result.

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# Example
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:

# Example
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# Example
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


# Return Values
# To let a function return a value, use the return statement:

# Example
# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example
# def myfunction():
#   pass



#  function with no arguments 
# def hello(data):
#     print("hello")
#     print(data)


#  blank function
#  boy mei pass keyword

#  function called
# hello(100)
# hello(200)

# v=200
# hello(v)
#  parameter


#  function with argument // more then one argument can pass.
def hello1(value,name):
    print(value)
    print(name)


# hello1(200,"kopal") # function calling



# array as argument.

def hello2(arrayvalue):
    for i in arrayvalue:
        print(i)


# hello2([1,2,3,4,5])

print("..........................................")

value1=[1,2,3,4,5]
# hello2(value1)


def even(x):
    if x%2==0:
        print("even")
    else:
        print("odd")  


# even(10)
# even(19)
# even(30)


def even1(x):
    i=1
    while i<=x:
        if i%2==0:
            print("even")
        else:
            print("odd")
        i=i+1

# even1(10)

def hello3(data, dictvalues):
    print(data)
    print(dictvalues)   

# hello3(230,{"name":"kopal","name2":"gangrade"})

# hello3(340,20,50)

# keyworded argument

def hello4(name,age):
    print(name)
    print(age)

# hello4(name="kopal",age=20)


# def hello5(*args,**kwargs):
#     print(list(args))
#     print(kwargs)


# hello5(100,900,300,name="kopal",lastname="gangrade")    

# hello5(2,"kopal",34,34.5)



# keyword argument
# *arg takes number , list ,tuple
# **kwargs --> dictionary

# recursion

# ek function called itself

# def printvalue(low,high):
#     for i in range(low,high+1):
#         print(i)
        

# printvalue(2,10)


def printvalue1(x):
    if(x==11):
        return
    printvalue1(x+1)
    print(x)
# printvalue1(1)


# def printvalue1(x):
#     if(x==0):
#         return
#     printvalue1(x-1)
#     print(x)

# printvalue1(10)

# printvalue1(1)--> printvalue1(2)-> printvalue1(3).....printvalue(10)
