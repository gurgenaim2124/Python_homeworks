import random

emojis = {
    1: '🟩',  # grass
    2: '🟦',  # pond
    3: '🏔️',  # hill
    4: '🌲'   # tree
}

grids = []

def generate_map(width, height):
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(random.randint(1, 4))

        grids.append(row)


    return grids
       
def generate_map_grid(grid):
    for row in grid:
        output = " "
        for cell in row:
            output += emojis[cell]
        # print(output) 

# print(generate_map_grid(generate_map(3,3)))