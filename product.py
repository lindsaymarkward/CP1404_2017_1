"""
Do this now (in pairs or threes):
Write a ProductList class that encapsulates a list of Products
Printing it should display the products nicely
Write methods for: add(Product), remove(Product),
total() -> float (get total price)
get_by_name(name) -> Product
"""
class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = " (on sale!)" if self.is_on_sale else ""
        return "{} ${:.2f}{}.".format(self.name, self.price, on_sale_string)

    def put_on_sale(self, discount):
        self.is_on_sale = True
        self.price -= self.price * discount

# p = Product("Phone", 340)
# print(p)
# p2 = Product("Taco", 8.7, True)
# print(p2)

# print(p, type(p))
# print(p.__eq__(Product()))

products = [Product("Phone", 200, False),
            Product("PC", 1420.95, False),
            Product("Plant", 24.5, True),
            Product('Bottle', 420.95, True)]

for product in products:
    print(product)

products[0].put_on_sale(.3)
print(products[0])

on_sale_products = [product.name for product in products if product.is_on_sale]
print(on_sale_products)
