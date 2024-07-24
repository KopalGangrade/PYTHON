#  how to represent object content
# dunder method(double underscore) or spacial method
# __str()__ (user) 

class car:
    def __init__(self, make,model,year ):
        self.make=make
        self.model=model
        self.year=year 
    def __str__(self):
        return(f"this is a {self.make},{self.model}car")
    
e1=car("veniu","#1sdg677",2020)
print(e1)

# __repr()__ (devloper) 

def __repr__ (self):
    return(f"make={self.make},model={self.model},year={self.year}")
c1=car("swift","#fjgk5656",2024)
print(c1)
# str(c1)
# c1.__repr__