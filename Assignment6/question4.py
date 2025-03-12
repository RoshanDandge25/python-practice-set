# 4. Design a system where a Library manages multiple Books, and each Book has an ID, title,
# and author.
# Functionalities:
# Add a Book to the library.
# Display all Books in the library.
# Exit the system when done.

class Book:
    def __init__(self, book_id ,title ,author):
       self.book_id=book_id
       self.title=title
       self.author=author

class Library:
    
    def __init__(self):
        self.books=[]
       
    def book_add(self ,book):
        self.books.append(book)
        print(f"Book {book.title} by {book.author} add sucessfully ")
    
    def display_book(self):
        if not self.books:
            print(" Sorry, no books available in the library.")
        else:
            print(" books in libraray")
        for book in self.books:
                print(f"ID is  {book.book_id} Title  {book.title} Author Nmae = {book.author}")
                
    def exits(self):
        print("thank you bye ")
        
def main():
    library=Library()
    
    while True:
        print('-'*20)
        print("Welcome to Libraray")
        print('-'*20)
        print("1.Add Book : ")
        print("2.Disply Books : ")
        print("3.Exit")
        print('-'*20)
        
        
        choice=input("Enter your choice :" )
        
        if choice=='1':
            book_id=input("Enter book Id : ")
            title=input("Enter book Title : ")
            author=input("Enter Book Author : ")
            
            book = Book(book_id , title ,author)
            library.book_add(book)
            
        elif choice=='2':
            library.display_book()
            
        elif choice =='3':
            library.exits()
            break
        else:
            print("invalid ")
if __name__=="__main__":
    main()
            
        