numbers = [-5, -2, 7, 8, 12, -1, 9, 15, 20]

print(f"before: {numbers}")

numbers[0] += -2
numbers[6] += 1
numbers[2] -= 1
print(f"after: {numbers}")

adds_5_elements = []

for num in numbers:
    adds_5_elements.append(num + 5)

print(f"final list: {adds_5_elements}")


