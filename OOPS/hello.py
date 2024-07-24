
#   defining class 
class game:
    pass


c1=game()
print(c1)
print(type(c1))
print(game)

#  class properties/or/attribute

class hello1:
    name="sima"


c2=hello1()
c2.name="kopal"
print(c2.name)




class student:
    name=" "
    id=123
    address='pune'
    age=20

s=student()
print(s.name)
print(s.id)
print(s.address)
print(s.age)

s.name="shiv"
s.id=345
s.address="mumbai"
s.age=23
print(s.name)
print(s.id)
print(s.address)
print(s.age)



class hello3:
    list1=[1,2,3]
    tuple1=(1,3,4,6)
    dct1={}

l2=hello3()
print(l2.list1)  # if list will empty so cant work indexing otherwise with element list can 
print(l2.tuple1)
print(l2.dct1)
l2.list1[0]=90
# l2.list1[1]=200

l2.list1.append(800)

print(l2.list1)
l3=hello3()
l4=hello3()




# ..............................................................................

#  constructure in python class


#  __init__   -----> constructor of class Hello...... alternet name is dunderd  init method
class Hello:
    def __init__(self, id,name ):
        self.id=id
        self.name=name
        

n1=Hello(465,"arzu")
print(n1.id,n1.name)




class Employee:                                  #class
    def __init__(self,name,id,address,company):   #construtor
        self.name=name
        self.id=id
        self.address=address
        self.company=company
 
    def printDetails(self):   #method
        print(self.name)
        print(self.id)
        print(self.address)
        print(self.company)    

E1=Employee("kopal",1234,"mumbai","meta")      #object
print(E1.name)

E1.printDetails()   # object.function

