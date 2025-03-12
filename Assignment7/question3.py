# 3. Create a class product having (pid and manufacture_location) as private
# fields,Create another class as Book having (name,
# number_of_pages,author,price) as private fields. Specify _init(), getters, setters,
# __str_() , print_data() Use correct OOP feature to implement this scenario.
# a) display the details of the product and book
# b) check if book price is 0 or negative then price is not valid otherwise print
# valid price.

class Product:
    def __init__(self , pid , manufacture_location):    
        self.__pid=pid
        self.__manufacture_location= manufacture_location

    def get_pid(self):
        return self.__pid
    
    def set_pid(self , pid):
        self.__pid=pid
    
    def get_manufacture_location(self):
        return self.__manufacture_location
    
    def set_manufacture_location(self ,manufacture_location):
         self.__manufacture_location = manufacture_location
    print('-'*50)
    def __str__(self):
        return f"Product Id : {self.__pid} \t Manufacture location : {self.__manufacture_location}"

      
class Book:
    def __init__(self ,name , number_of_pages , author , price ):
        self.__name=name
        self.__number_of_pages=number_of_pages
        self.__author=author
        self.__price=price
        
    
    
    def get_name(self):
        return self.__name
    
    def set_name(self , name):
        self.__name=name
        
    def get_number_of_pages(self):
        return self.__number_of_pages
    
    def set_number_of_pages(self , number_of_pages):
        self.__number_of_pages=number_of_pages
    
    def get_author(self):
        return self.__author
    
    def set_author(self , author):
        self.__author=author
        
    def get_price(self):
        return self.__price
    
    def set_price(self , price):
        self.__price=price
        
        
    def set_price(self ,price):
        if price<=0:
            print(f" something wrong Enter vald price  {price}")
        else:
            print(f"valid price  {price}")
            self.__price=price
     
    def __str__(self):
        return f"Book Name = {self.__name } '\n' Number of Pages = {self.__number_of_pages} '\n' Author Name = {self.__author} '\n' Price = {self.__price} "   
    
           

p=Product(1 , "Pune")

book=Book("CHHAVA" , 864 , "Shivaji_Savant" , 1000)

print(p)
print('-'*50)
print(book)
print('-'*50)

book.set_price(-10)
print('-'*50)
book.set_price(900)
print('-'*50)
print(book)
