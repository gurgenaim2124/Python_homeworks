countries = {
    "Georgia": "Tbilisi",
    "America": "Washington",
    "France": "Paris",
    "Italy": "Rome",
    "Spanish": "Madrid"
}

for key in countries.keys():
    print(key)

print("-" * 10 )

for values in countries.values():
    print(values)

print("-" * 10 )

for key, values in countries.items():
    print(f"The capital of {key} is {values}")

swapped = {value: key for key, value in countries.items()}
print(swapped)

print("-" * 10)

for key, values in swapped.items():
    print(f"The capital of {values} is {key}")
