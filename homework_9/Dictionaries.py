product = {"name": "Keyboard", "units_sold": 5, "unit_price": 20.0}
unit_sold = product["units_sold"]
unit_price = product["unit_price"]
print(f"{unit_sold} * {unit_price} = {unit_sold * unit_price}")

product["region"] = "North"
print(product)

product["units_sold"] = 10 
print(product)

for key, value in product.items():
    print(f"{key}, {value}")

product_dict = [
    {"Phone": "Iphone 15 pro", "price": 2000, "stock": 20},
    {"Phone": "Iphone 14 pro", "price": 1800, "stock": 15},
    {"Phone": "Iphone 13 pro", "price": 1300, "stock": 10}
]

total_revenue = 0 
for product in product_dict:
    total_revenue += product["price"] * product["stock"]

print(total_revenue)