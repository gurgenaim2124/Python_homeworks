
odd_numbers = []
numbers_divisible_by_seven = []



while True:
    user_input = input("Enter a number or type 'Done' to quit: ")
    if user_input.lower() == "done":
        print("Thank you")
        break

    num = int(user_input)
    if num % 2 == 1:
        odd_numbers.append(num)
    if num % 7 == 0:
        numbers_divisible_by_seven.append(num)

odd_numbers.sort()
numbers_divisible_by_seven.sort()
print(f"{odd_numbers = }")
print(f"{numbers_divisible_by_seven = }")