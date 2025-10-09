while True:
    user_password = input("Enter your password: ")

    password_contains_upper_case = any(c.isupper() for c in user_password)
    password_contains_lower_case = any(c.islower() for c in user_password)
    password_contains_number = any(c.isdigit() for c in user_password)
    password_contains_special_character = any(not c.isalnum() for c in user_password)


    if not password_contains_lower_case:
        print("Please include lower case")
        continue
    elif not password_contains_upper_case:
        print("Please include upper case")
        continue
    elif not password_contains_number:
        print("Please include numbers")
        continue
    elif not password_contains_special_character:
        print("Please include special characters")
        continue
    elif len(user_password) < 8:
        print("Passwrod must be at least 8 characters long")
        continue
    else:
        print("User created!")
        break
