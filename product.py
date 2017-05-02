"""
Do this now (in pairs or threes):
Write a ProductList class that encapsulates a list of Products
Printing it should display the products nicely
Write methods for: add(Product), remove(Product),
total() -> float (get total price)
get_by_name(name) -> Product
"""
# Now: Write a FoodItem class that extends Product meaningfully


class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = " (on sale!)" if self.is_on_sale else ""
        return "{} ${:.2f}{}.".format(self.name, self.price, on_sale_string)

    def put_on_sale(self, discount):
        # discount is specified as decimal, 0.31 = 31%
        self.is_on_sale = True
        self.price -= self.price * discount

    def __add__(self, other):
        name = self.name + ' ' + other.name
        price = self.price + other.price
        return Product(name, price)

    def __lt__(self, other):
        return self.price < other.price

    def __getitem__(self, item):
        return self.name * item

def run_tests():
    p1 = Product("Phone", 340)
    p2 = Product("Taco", 8.7, True)
    print(p1, p2)
    p3 = p2 + p1
    print(p3)
    print(p1 < p2)
    print(p1[7])


    # products = [Product("Phone", 200, False),
    #             Product("PC", 1420.95, False),
    #             Product("Plant", 24.5, True),
    #             Product('Bottle', 420.95, True)]
    #
    # for product in products:
    #     print(product)
    #
    # products[0].put_on_sale(.3)
    # print(products[0])
    #
    # on_sale_products = [product.name for product in products if product.is_on_sale]
    # print(on_sale_products)

if __name__ == '__main__':
    run_tests()
