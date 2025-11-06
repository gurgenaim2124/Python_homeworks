products = ["Keyboard", "Mouse", "Monitor", "Speaker", "Webcam"]


print(products[0], products[-1])

products.append("Headphones")
print(products)

products.remove("Speaker")
print(products)

for product in products:
    print(product.upper())

print(f"total number in list {len(products)}")

print(f"slicing: {products[:3]}")

products.sort()
print(f"sorting with alphabetic: {products}")