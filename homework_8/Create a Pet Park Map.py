import random

emojis = {
    1: '🟩',  # grass
    2: '🟦',  # pond
    3: '🏔️',  # hill
    4: '🌳'   # tree
}

grids = []


def generate_emoji(rows, columns):

    areas = {
                'grass': "🟩",
                'pond':'🟦',
                'hill': '🏔️',
                'tree':'🌳'
            }

    for _ in range(rows):
        row = []

        for _ in range(columns):
            cell = random.choice(list(areas.values()))
            row.append(cell)

        grids.append(row)

    return grids

def print_grid_for_emojis(grid):
    for row in grid:
        print(" ".join(row))
    



print(print_grid_for_emojis(generate_emoji(3,3)))         

                   

