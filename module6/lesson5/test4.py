# #
# Library System
# Build a simple library system using a class. Each book is an object. Your system lets users borrow and return books and tracks whether each book is currently available.

# What you need to use
# ------------------------------------------------------------------------
# 1.  Book class      →  __init__ sets title, author, and is_borrowed = False
# 2.  borrow()        →  sets is_borrowed to True and prints a confirmation
# 3.  return_book()   →  sets is_borrowed to False and prints a confirmation
# 4.  3 Book objects  →  demonstrate both borrow() and return_book()
# 5.  self            →  used to access and update attributes inside methods
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Book class with __init__ setting title, author, is_borrowed   →   5 marks
# 2.  borrow() sets is_borrowed True and prints confirmation         →  10 marks
# 3.  return_book() sets is_borrowed False and prints confirmation   →  10 marks
# 4.  At least 3 Book objects with both methods demonstrated         →  10 marks
# 5.  Program runs without any errors                                →   5 marks
# ========================================================================
# Total  →  40 marks
# # ========================================================================
class Book:
    def __init__(self , author ,title ,  is_borrowed = False ):
        self.author = author
        self.title = title
        self.is_borrowed = is_borrowed
    def borrow(self ):
        self.is_borrowed = True
        print("This book is borrowed")
    def return_book(self):
            self.is_borrowed = False
            print("This book has been returned")
b1 = Book("JK Rowling" , "Harry Potter Chamber of Secrets")
b1.borrow()
b2 = Book("Herge" , "Tintin in Tibet" )
b2.borrow()
b2.return_book()
b3 = Book("Roald Dahl" , "Big Friendly Giant")
b3.borrow()