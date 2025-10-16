def numeric_input():
    user_input = input("Enter number: ")
    try:
        num = float(user_input) 
        print(f"{num} is a valid number")
        return num
    except ValueError:
        print("Please enter a valid number")
        return None  

number = numeric_input()

