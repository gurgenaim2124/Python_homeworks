user_input = float(input("Enter some number: "))

if user_input % 2 == 0:
    print("it's Even")
else:
    print("it's Odd")

print("Large" if user_input >= 100 else "small")