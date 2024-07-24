

#A class is a blueprint or a template for creating object, providing initial values for states (member ,variable and attributes),
# and implementations of behavior (member function or methods). The user - defined objects are cretaed using the class keyword.\

# Creating a Class

# class details:
#     name="rohan"
#     age=20


# Creating an Object

# Object is the instance of the class usesd to access the properties of the class.

# obj1= details()

# example

# class details:
#     name="rohan"
#     age=20
# obj1= details()
# print(obj1.name)
# print(obj1.age)  

# SELF PARAMETER

# the self parameter is a reference to the current instance of the class, and is used to access
#  variables that belongs to the class.

# it must provided as the extra parameter inside the method definition.

# example

# class details:
#     name="rupal"
#     age=21
#     def desc(self):
#         print("my name is",self.name, "and i'm",self.age,"year old.")
# obj1=details()
# obj1.desc()





class person:     #  class
    name="komal"
    occupation="software devloper"
    salary=9000000
    def info(self):     # self parameter
        print(f"{self.name} is a {self.occupation}")

a=person()   #object
b=person()
a.name="kopal"
a.occupation="busniess women"

b.name="himanshi"
b.occupation="business girls"
# print(a.name,a.occupation)

a.info()
b.info()
