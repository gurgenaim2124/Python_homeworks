names = ["Giorgi", "Luka", "Nika", "Lazare", "Dachi", "Achi", "Aleqsandre", ]

name_add = input("add name: ")

names.append(name_add)

print(names)

remove_name = input("remove a name ")

names.remove(remove_name)
print(names)

search_name = input("search name ")

if search_name in names:
    print(f"{search_name} is in your list")
else:
    print(f"{search_name} is't in your list")

user_input = input("do you want to Display all names in alphabetical order ")

if user_input == "yes".lower():
    for a in sorted(names):
     print(names)


# esec ver gavige
