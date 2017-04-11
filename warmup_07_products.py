__author__ = 'Lindsay Ward'

products = [["Phone", 340, False],
            ["PC", 1420.95, False],
            ["Plant", 24.5, True],
            ['Bottle', 420.95, True]]
# print(products)

# for loop version
on_sale_products = []
for product in products:
    if product[2]:  # if product is on sale
        on_sale_products.append(product)
print(on_sale_products)

# list comprehension version
on_sale_products = [product[0].lower() for product in products if not product[2]]
print(on_sale_products)
