class Book:
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print(f"Book object with id {self.bid} is deleted")

    def showBook(self):
        print(f"ID: {self.bid}, Name: {self.bname}, Price: {self.price}, Author: {self.author}")

# Example
b1 = Book(101, "Python Basics", 450, "Guido")
b1.showBook()
