# 1. Write a Python program to create a Vehicle class with max_speed and
# mileage instance attributes.
# Write a python program to Create a child class Bus that will inherit all of the
# variables and methods of the Vehicle class.


class Vehicle:
    def __init__(self , max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
    def Details_print(self):
        print("IN PARENT CLASS ")
        print(f"max speed = {self.max_speed}")
        print(f" mileage = {self.mileage}")
print('-'*50)
class Bus(Vehicle):
    def __init__(self , max_speed , mileage):
        super().__init__( max_speed , mileage)
       
        
    def Details_print(self):
        print('-'*50)
        print("IN CHILD CLASS ")
        print(f"max speed = {self.max_speed}")
        print(f" mileage = {self.mileage}")
    
vec=Vehicle(56 , 85 )
vec.Details_print()

bus=Bus(98 , 56)
bus.Details_print()
        