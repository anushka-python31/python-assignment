class Product:
    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"Product object with id {self.pid} is deleted")

    def showProduct(self):
        print(f"ID: {self.pid}, Name: {self.pname}, Price: {self.price}, Quantity: {self.quantity}")

# Example
p1 = Product(201, "Laptop", 55000, 5)
p1.showProduct()
