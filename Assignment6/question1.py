# 1. Create a class named Mobile with attributes ModelName,Company,Price and with
# methods:set_attributes, print_details and can_afford

class Mobile:
    def __init__(self , ModelName ,Company ,Price):
        self.__ModelName=ModelName
        self.__Company=Company
        self.__price=Price
    
    def set_ttribute(self , ModelName ,Company ,Price):
        self.__ModelName=ModelName
        self.__Company=Company
        self.__price=Price 
    
    def print_details(self):
        print(f"Model Name = {self.__ModelName}")
        print(f"Company Name = {self.__Company}")
        print(f"Mobile Price ={self.__price}")
    
    def can_afford(self , budget):
        if self.__price <=budget:
            print("Congrats you can afford mobile ")
        else:
            print("Sorry ! You cant affort mobile ")
        
        
mob=Mobile("Samsung s 24" ,"Samsung" , 250000)
mob.print_details()
mob.can_afford(2400000)
print("-------------------------- ")
print("After value change")
mob.set_ttribute("Iphone16" , "Apple", 12000)
mob.print_details()
mob.can_afford(24000)
