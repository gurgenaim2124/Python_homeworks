
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



