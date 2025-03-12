# <!-- 2. Write a Rectangle class in Python language, allowing you to build a rectangle
# with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a
# Area() method to calculate the area of the rectangle.
# Create a method display() that display the length, width, perimeter and area of
# an object created using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with
# a attribute and another Volume() method to calculate the volume of the
# Parallelepiped. -->

class Rectangle:
    def __init__(self , length , width ):
        self.length=length
        self.width=width
        
    def perimeter(self):
        return 2*(self.length + self.width)
    
    def Area(self):
        return self.length * self.width
    
    def display_fun(self):
        print('-'*50)
        print(f" perimeter of rectangle = {self.perimeter()}")
        print(f" Area of rectangle = {self.Area()}")
        
        
class Parallelepiped(Rectangle):
    def __init__(self, length, width , height):
        super().__init__(length, width)
        self.height=height
        
    def Volume(self):
       return self.length * self.width * self.height
 
l=int(input("Enter length : ") )
w=int(input("Enter width : ") )     
rect=Rectangle(l, w)
rect.display_fun()
print('-'*30)
h=int(input("Enter height : ") )
parallel = Parallelepiped(l , w ,h)
print(f"Volume of Rectangle is : {parallel.Volume()}")


        
