products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics", "stock": 15},
    {"name": "T-shirt", "price": 25, "category": "Clothing", "stock": 50},
    {"name": "Phone", "price": 800, "category": "Electronics", "stock": 30},
    {"name": "Shoes", "price": 60, "category": "Clothing", "stock": 40},
    {"name": "Book", "price": 15, "category": "Stationery", "stock": 100}
]   


def search_product (search_term):
    for items in products:
        if items["name"].lower() == search_term.lower() or items["category"].lower() == search_term.lower():
            print(f"Name: {items['name']}, Category: {items['category']}")
            return True
        else:
            return print("try again")



def filter_products(max_price=None, min_stock=None):
    filtered = []

    for product in products:
        if max_price is not None and product["price"] < max_price:
            filtered.append(product)
        elif min_stock is not None and product["stock"] > min_stock:
            filtered.append(product)

    return filtered



while True:

    user_input = input("Enter product name or category: ")
    if user_input == "done":
        print("goodbye")
        break
    search_product(user_input)


    user_choice = input("Do you want to filter by 'price' or by 'stock'? ").lower()

    if user_choice == "price":
        max_price = float(input("Enter maximum price: "))
        result = filter_products(max_price=max_price)
        print(f"\nProducts cheaper than {max_price}:")
        for p in result:
            print(p)

    elif user_choice == "stock":
        min_stock = int(input("Enter minimum stock amount: "))
        result = filter_products(min_stock=min_stock)
        print(f"\nProducts with stock above {min_stock}:")
        for p in result:
            print(p)

    else:
        print("Invalid option. Please choose 'price' or 'stock'.")




total_value = 0

for p in products:
    total_value += p["price"] * p["stock"] 

print(f"Total value of all products {total_value}")
        