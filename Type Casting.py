def to_integer(text):
    try:
        return int(text)
    except:
        return "Wrong"


user_input = input("Write a number ")
print(to_integer(user_input))
