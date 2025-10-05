random_numbers = [32, 43, 54, 12,57, 12, 23, 24]

for char in random_numbers:

    print(char)

print(f"lenght = {len(random_numbers)}")

sum = 0

for i, ev in enumerate(random_numbers):
    sum += ev

print(f"this is sum of all elements {sum}")
print(f"this is average of all elements {round(sum / len(random_numbers))}") 
print(f"this is minimum value in the elements {min(random_numbers)} and this is maximum value {max(random_numbers)}")
