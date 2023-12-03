from utils import input

input = input.text_to_string("2")

games = input.split("\n")

limits = { "red": 12, "green": 13, "blue": 14 }

def replace_if_higher(highest_values, amount, colour):
    if highest_values[colour] < amount:
        highest_values[colour] = amount
    
    return highest_values

cube_set_powers = []

def calc_cube_set_power(values):
    return values["red"] * values["green"] * values["blue"]

for game in games:
    id, information = game.split(":")
    id = id.split(" ")[1]
    information = information.strip()

    handfuls = information.split(";")

    highest_values = {"red": 0, "green": 0, "blue": 0}

    for handful in handfuls:
        cube_groups = handful.strip().split(", ")
        for cube_group in cube_groups:
            amount, colour = cube_group.split(" ")
            highest_values = replace_if_higher(highest_values, int(amount), colour)

    cube_set_powers.append(calc_cube_set_power(highest_values))

answer = sum(cube_set_powers)

print(f"Solution: {answer}")