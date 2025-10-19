import datetime

# def numeric_input():
#       while True:
#         user_input = input("Enter number: ")
#         dot_found = False
#         valid = True

#         for ch in user_input:
#             if ch == ".":
#                 if dot_found:
#                     valid = False
#                     break
#                 else:
#                     dot_found = True
#             elif not ch.isdigit():
#                 valid = False
#                 break

#         if valid:
#             print(f"{user_input} is a valid number")
#             break
#         else:
#             print("Try again")
            
# number = numeric_input()

# def alphabetic_characters():
#     while True:
#         user_input = input("Enter your name: ")
        
#         name = user_input

#         if name.isalpha():
#             print(f"{name} is valid name")
#             break
#         else: 
#             print("Please enter valid name!")
#             continue

# names = alphabetic_characters()

def is_valid_format():
    user_input = input("Enter date (YYYY-MM-DD): ")
    data = user_input.split(" ")
    year, month, day = data
    if len(data) != 3:
        return False
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        print("Try again")
        return False

    month = int(month)
    if month < 1 or 12 < month:
        return False
    day = int(day)
    if day < 1 or 31 < day:
        return False
    final_date = datetime.datetime.strptime(user_input, "%Y %m %d")

    return print(final_date)

date_input = is_valid_format()