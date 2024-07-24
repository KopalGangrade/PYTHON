# class dogs:   #classs name
#     pass
#     def __init__ (self,name,color,age,breed):   #constructor 
#         self.name=name
#         self.color=color  #attribute
#         self.age=age
#         self.breed=breed
#     def barking(self):   #method
#         print("bho bho")


# class dogs:
#     pass
# d1=dogs()
# print(d1)
# print(id(d1))

#name - mangling function

class Employee:                                  #class
    def __init__(self,name,id,address,company):   #construtor
        self.__name=name
        self.__id=id
        self.address=address
        self.company=company
 
    def __printDetails(self):   #method
        print(self.name)
        # print(self.id)
        # print(self.address)
        # print(self.company)    

E1=Employee("kopal",1234,"mumbai","meta")      #object
# print(E1.name)
E1.__printDetails() 
        


