user_list = []

while True:
    user_input = (input("Add a number to the list: "))

    # if user_input.lower() == "quit":
    #     print("Final list", user_list)
    #     break

    numbers = user_input.split(',')

    for num in numbers:
        num = num.strip()
        if num.isdigit():
            user_list.append(int(num))
        else:
            print(f"{num} is not a valid number, skipped.") 
    print("Current list:", user_list)

    # remove list 

    user_remove_number = input("do you want to remove a number from the list?: ")

    if user_remove_number.lower() == "yes":
        number_to_remove = input("Enter which number do you want to delete? ").strip()
   
        if number_to_remove.isdigit():
            number_to_remove = int(number_to_remove)
            if number_to_remove in user_list:
                user_list.remove(number_to_remove)
                print(f"{number_to_remove} removed successfully")
                print(f"current list {user_list}")
            else: 
                print(f"{number_to_remove} is not in the list")
        else :
            print("invalid input try again")
    elif user_remove_number.lower() == "no":
        print("okay continuing...")

        
    

    # clear or not

    list_cleaner = input("do you want to clear the list ? ")

    if list_cleaner.lower() == "yes":
        user_list.clear()
        print("List has been cleared completely!")
    elif list_cleaner.lower() == "no":
        print("Okay continuing...")
    elif list_cleaner == int or float:
        print("Please enter yes or no")
    else:
        print("Please enter valid sentence")

    # sum and average

    if user_list:
        total = sum(user_list)
        average = round(total / len(user_list))
        print(f"Sum: {total} and Average: {average}")
        print(f"Minimum value: {min(user_list)} and Maximum value: {max(user_list)}")
    else:
        print("No numbers in the list")
        
    # quiting 

    user_exit = input("Do you want to exit the program ? ")

    if user_exit.lower() == "yes":
        print("You've successfully exited the program") 
        print("Goodbye...")
        break
    elif user_exit.lower() == "no":
        print("Okay start again...")
        continue
    else:
        print("Please enter valid sentence")