# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         if isinstance(value, str) or value <= 0:
#             raise ValueError("Positive number expected")
#         self._radius = value


# val1 = circle(45)
# print(val1._radius)
# val2 = circle(-6)
# print(val2._radius)


# slots are used for making memory efficient.
# 1] memory efficienxy incresses.
# 2]cant assign instance attributes dynamically.
# 3] omit __dict__ attribute of every instance.


class points:
    __slots__=("x","y")
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(s1,s2):
        d=(s2.x-s1.x)**2+(s2.y-s1.y)**2
        print(d**0.5)
p1=points(3,5)
# p1.z=43
p2=points(8,7)
from pympler import asizeof 
print(asizeof.asizeof(p1))

p1.distance(p2)
p2.distance(p1)

