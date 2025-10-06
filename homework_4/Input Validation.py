while True:
    while True:
        user_input = input("Enter number: ")

        if user_input.isdigit():
            number = int(user_input)
            break
        else:
            print("Please enter a number ")

    while True:
        user_input = input("Enter second number: ")
        
        if user_input.isdigit():
            number2 = int(user_input)
            break
        else: 
            print("Please enter a correct number")
    
    while True:
        user_input = input("choose a operation (+, -, *, /) ")
        number = number
        number2 = number2
        if user_input == "+":
            result = f"{number} + {number2} = {number + number2}"
            break
        elif user_input == "-":
            result = f"{number} - {number2} = {number - number2}"
            break
        elif user_input == "*":
            result = f"{number} * {number2} = {number * number2}"
            break
        elif user_input == "/":
            result = f"{number} / {number2} = {number / number2}"
            break
        else:
            print("please enter given operation ")

# es ver gavige 

    print(number)
    print(number2)
    print(result)