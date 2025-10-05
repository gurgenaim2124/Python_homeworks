import random
Attempts = 0 

while True:

    user_input = int(input("Guess the number between 1 and 20: "))
    secret_number = random.randint(1, 20)
    Attempts += 1

    if user_input < 1 or user_input > 20:
        print("please enter a number between 1 to 20 : " "try again") 
        continue

    if user_input == secret_number:
        print(f"'Correct'  you guessed it in {Attempts} tries ")
        
        break
    
    elif user_input < secret_number:
        print("too low")

    elif user_input > secret_number:
        print("too high")



