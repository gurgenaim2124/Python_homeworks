import random
numbers = []
for _ in range(20):
    numbers.append(random.randint(0, 40))

print(numbers)

# def liner_search():
#     for i, number in enumerate(numbers):
#         if number == 7:
#             print(f"i have found it on {i} index")
#             return i
#     print("Not found")
#     return -1
       
# num = liner_search()

def liner_search_different_values(number, target):
    for i , number in enumerate(numbers):
        if number == target:
            print(f"i have found it on {i} index")
            return i
    print("not found")
    return -1

liner_search_different_values(numbers, 8)
liner_search_different_values(numbers, 10)
liner_search_different_values(numbers, 15)
liner_search_different_values(numbers, 2)
