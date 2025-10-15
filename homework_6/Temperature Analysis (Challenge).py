temperatures = [-15, -16, -17, -16.5, -16.7, -17.1, -15.3, -15, 32, 33]
tuple_temp = []
for i, temperature in enumerate(temperatures, start= 1):
    tuple_temp.append((i,temperature))
    
    
print(f"Tuple list: {tuple_temp}")
    
# dict_temp = dict(tuple_temp)

# for day, temp in dict_temp.items():
#     print(f"Day {day}: {temp}")


while True:
    user_input = (input("Do you want add another temperature: "))
    if user_input.lower() == "no":
        print("okey you can countinue")
    if user_input.lower() == "yes":
        temperatures.append(int(user_input))
    print(temperatures)

    user_sum = (input("Do you want to find average of temperature ? "))
    if user_sum.lower() == "yes":
        total = round(sum(temperatures) / len(temperatures))
        print(total)
    if user_sum.lower() == "no":
        print("okay you can continue ... ")


    user_temp = int(input("Enter temperature threshold: "))

    print("Days with temperatures above threshold:")
    for day, temp in enumerate(temperatures, start=1):
        if user_temp < temp: 
            print(f"Day {day}: {temp}")       
            

    user_ascneding_descending = input("How would you like the temperatures to be sorted: ascending or descending? ")

    if user_ascneding_descending.lower() == "ascending":
       print(sorted(temperatures))
    elif user_ascneding_descending.lower() == "descending":
        print(sorted(temperatures, reverse=True))
    else:
        print("Invalid choice. Please type 'ascending' or 'descending'.")