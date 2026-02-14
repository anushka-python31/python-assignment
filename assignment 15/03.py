class Shirt:
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Shirt object with id {self.sid} is deleted")

    def showShirt(self):
        print(f"ID: {self.sid}, Name: {self.sname}, Type: {self.type}, Price: {self.price}, Size: {self.size}")

# Example
s1 = Shirt(301, "Formal Shirt", "Formal", 1200, "Large")
s1.showShirt()
