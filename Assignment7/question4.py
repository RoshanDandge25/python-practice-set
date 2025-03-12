# 4. Write a Class Painting with method calculatePaintingCost. Write a Class
# FlatPainting with noOfRooms which is inheritated from Class Painting. Override
# calculatePaintingCost. (Assume per room painting cost is 10000).
# Write a Class BulidingPainting with noOfFlats which is inheritated from Class
# Painting. Override calculatePaintingCost. (Assume per Flats painting cost is
# 25000) Write method for 1.Flat 2.Building and then calculate the cost according
# to the type.


class Painting:
    def calculatePaintingCost(self):
        pass  # This will be overridden in the child classes

class FlatPainting(Painting):
    def __init__(self, noOfRooms):
        self.noOfRooms = noOfRooms

    def calculatePaintingCost(self):
        return self.noOfRooms * 10000  # Per room painting cost is 10,000

class BuildingPainting(Painting):
    def __init__(self, noOfFlats):
        self.noOfFlats = noOfFlats

    def calculatePaintingCost(self):
        return self.noOfFlats * 25000  # Per flat painting cost is 25,000

# Taking user input for type of painting
print("Choose type of Painting:")
print("1. Flat Painting")
print("2. Building Painting")
choice = int(input("Enter choice 1 or 2: "))

if choice == 1:
    noOfRooms = int(input("Enter number of rooms: "))
    flat = FlatPainting(noOfRooms)
    print("Total painting cost for flat:", flat.calculatePaintingCost())

elif choice == 2:
    noOfFlats = int(input("Enter number of flats: "))
    building = BuildingPainting(noOfFlats)
    print("Total painting cost for building:", building.calculatePaintingCost())

else:
    print("Invalid choice!")
