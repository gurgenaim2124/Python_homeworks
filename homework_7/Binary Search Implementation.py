numbers = [14, 10, 46, 50, 26, 43, 39, 44, 33, 43, 0, 7, 19, 34, 31, 24, 11, 37, 19, 11]
numbers.sort()

print(numbers)

def binary_search(numbers, target):

    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = low + (high - low) // 2 

        if numbers[mid] == target:
            print(f"i have found it on {mid} index")
            return mid

        if numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print("not found")
    return -1
    
binary_search(numbers, 24)
binary_search(numbers, 37)
binary_search(numbers, 12)
binary_search(numbers, 43)

