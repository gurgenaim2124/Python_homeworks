import random

numbers = []

for i in range(20):
    numbers.append(random.randint(-100, 100))
print(numbers)

positive_numbers = []
for num in numbers.copy():
    if num > 0:
        positive_numbers.append(num)
       

print(f"{positive_numbers = }")

negative_numbers = []
for num in numbers.copy():
    if num < 0: 
        negative_numbers.append(num)
       

print(f"{negative_numbers = }")

even_numbers = []
odd_numbers = []
for number in numbers.copy():
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
        

print(f"{even_numbers = }")
print(f"{odd_numbers = }")

divisible_by_5 = []
for num in numbers.copy():
    if num % 5 == 0:
        divisible_by_5.append(num)

print(f"{divisible_by_5 = }")