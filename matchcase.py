# import os
# print("hello world from ...")
# os.system("python --version")



# To  implement switch case like characteristics very similar to if else functionallity, we use a match case in python.

# A match statment will compare a given variable's value to different shapes, also referred to as the pattern. the main idea
# is ton keep on coming the variable with all the present patterns until it fits into one.

#///////  matchcase syntax  /////////
# match argument:
#         case 0:
#             return "zero"
#         case 1:
#             return "one"
#         case 2:
#             return "two"
#         case default:
#             return "something"
    

x=int(input("enter a number of x"))
match x:
    case 0:
        print("x is zero")
    case 4 if x%2==0:
        print("x%2==0 and case is 4")
    case _ if x< 10:
        print("x is <10")
    case _ :
        print(x)
