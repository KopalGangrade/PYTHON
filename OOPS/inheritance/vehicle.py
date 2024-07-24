# class vehicle:
#     total = 0
#     def __init__(self, make, model, year):
#         type(self).total += 1
#         self.make = make
#         self.model = model
#         self.year = year
#         self.started = False

#     def start(s):
#         s.stared = True
#         print("starting engine")


# class car(vehicle):
#     def __init__(self, make, model, year, no_seats):
#         super().__init__(make, model, year)
#         self.no_seats = no_seats

#     def Drive(s):
#         s.start()
#         print("Car is Started.")

#     def Stop(s):
#         s.started = False
#         print("Car has Stopped")


# class motercylce(vehicle):
#     def __init__(self, make, model, year, no_vehicle):
#         super().__init__(make, model, year)
#         self.wheels = no_vehicle

#     def Ride(s):
#         s.Start()
#         print("Bike is Started.")


# q1 = car("Ford", "Camry", 1992, 4)
# print(q1)
# print(f"my car is",{"venue",})




class employee:
    def __init__(self,id,name,salary,department):
        self.id=id
        self.name=name
        self.salary=salary
        self.department=department
    def cal_sall(self,hour):
        if hour>50:
            extra=(hour-50,)