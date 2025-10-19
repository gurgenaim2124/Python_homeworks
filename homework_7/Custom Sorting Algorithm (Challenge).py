
def sort_list(items, order="ascending"):
    if order == "ascending":
        return sorted(items)
    elif order == "descending":
        return sorted(items,reverse=True)
    else:
        return "Invalid order! Choose 'ascending' or 'descending'."

numbers = [4, 6, 8, 1, 3, 5]
print(sort_list(numbers, "ascending"))
print(sort_list(numbers, "descending"))

# Include a parameter to sort by a specific key function (similar to the key parameter in Python's built-in sort)
# Demonstrate your sorting algorithm with different types of data (numbers, strings, custom objects)
# Compare your algorithm's efficiency with Python's built-in sorting functions

# es sami ver vqeni
