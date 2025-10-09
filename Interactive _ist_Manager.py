user_list = []

while True:
    user_input = (input("Add a number to the list or 'Quit': "))

    if user_input.lower() == "quit":
        print("Final list", user_list)
        break

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
        number_to_remove = input("Enter which number do you want to delete? ")
   
        if number_to_remove.isdigit():
            sum_list = 0
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
        print("okay goodbye")
        break
    
    # sum and average

    if user_list:
        total = sum(user_list)
        average = round(total / len(user_list))
        print(f"Sum: {total} and Average: {average}")
    else:
        print("No numbers in the list")