
random_number = int(input("Enter random number "))

if random_number % 2 == 0:
	print("Even")
elif random_number % 2 == 1:
	print("Odd")
else:
	print("Error")

print("-" * 100)
 
persons_age = int(input("Enter your age "))
age_left_to_vote = 18 - persons_age

eligible_vote = "you can vote" if persons_age >= 18 else f"You can in {age_left_to_vote} years "

print(eligible_vote)

print("-" * 100)

temp = int(input("enter current temeraputre "))

if 0 <= temp and temp <= 10:
    print("It's cold")
elif 10 < temp and temp <= 20:
    print("kinda hot")
elif 20 < temp and temp <= 30:
    print("Hot")
elif 0 >= temp and temp >= -10:
    print("cold weather")
elif -10 > temp and temp >= -20:
    print("it's freezing")