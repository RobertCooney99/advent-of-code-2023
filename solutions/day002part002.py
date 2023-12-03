from utils import input

input = input.text_to_string("2")

games = input.split("\n")

def replace_if_higher(highest_values, amount, colour):
    highest_values[colour] = max(highest_values[colour], amount)
    return highest_values

def calc_cube_set_power(values):
    return values["red"] * values["green"] * values["blue"]

def calc_cube_set_powers():
    powers = []
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

        powers.append(calc_cube_set_power(highest_values))

    return powers


cube_set_powers = calc_cube_set_powers()

answer = sum(cube_set_powers)

print(f"Solution: {answer}")