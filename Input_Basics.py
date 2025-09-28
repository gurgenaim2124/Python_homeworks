def user_age(text): 
    try:
        age = int(text)
        if age < 0 :
            return "Error lol "
        elif age >= 18:
            return "You are an adult"
        else:
            return "You are a minor"
    except ValueError:
        return "invalid input, write a number"
    

user_input = input("Enter your age ")
print(user_age(user_input))


# def user_age(text):
#     try:
#         age = float(text) 
#         if age < 0:
#             return "Error: age cannot be negative"
#         elif age >= 18:
#             return "You are an adult"
#         else:  
#             return "You are a minor"
#     except ValueError:
#         return "Invalid input! Please enter a number."


# user_input = input("Enter your age: ")
# print(user_age(user_input))


