def input_number():
    number = int(input("Enter number: "))
    return number

num = input_number()
print(num)

def input_string():
    string = input("Enter your name: ")
    return string

name = input_string()
print(name)

def input_list():
    user_list = (input("Enter some numbers: "))
    str_list = user_list.split(",")

    num_list = [int(x.strip()) for x in str_list]
    return num_list
    
listing = input_list()
print(listing)


# def multiple_tuples():
#     screen_size = (1920, 1080, 1280, 960)

#     for i, item in enumerate(screen_size):
#         print(f"{i}, {item}")

#     return screen_size

# multiple_tuples()

def screen_resolution():
    width = 1920
    height = 1080
    depth = 32
    refresh_rate = 60
    return width, height, depth, refresh_rate 

w, h, d, r = screen_resolution()  
print(f"Width: {w}, Height: {h}, Depth: {d}, Refresh rate: {r}")
