users_word = input("Enter some words ")
vowels = "aeiou"

for char in users_word:
    print(char)

for letter in users_word:
    if letter in vowels:
        print(f"vowels ->{letter}")

for char in reversed(users_word):
    print(char)