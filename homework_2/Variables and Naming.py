stadium_cost = 350
person = 22
one_person_money = round(stadium_cost / person)
balance = person * one_person_money

print(f"{person} wants to play a football, but stadium cost {stadium_cost} gel")
print(f"if they want to play football a single person needs to pay {one_person_money} gel")
print(f"after they collected money balance was {balance} gel ") 
print(f"When they paid the amount, they had {balance - stadium_cost} left") 
