from utils import input

input = input.text_to_string("2")

games = input.split("\n")

def replace_if_higher(highest_values, amount, colour):
    if highest_values[colour] < amount:
        highest_values[colour] = amount
    
    return highest_values

def is_game_possible(limits, highest_values):
    is_possible = True
    for colour in limits:
        if highest_values[colour] > limits[colour]:
            is_possible = False
    return is_possible

def calc_possible_games_ids(limits):
    possible_game_ids = []
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

        if is_game_possible(limits, highest_values):
            possible_game_ids.append(int(id))

    return possible_game_ids

limits = { "red": 12, "green": 13, "blue": 14 }
possible_game_ids = calc_possible_games_ids(limits)

answer = sum(possible_game_ids)

print(f"Solution: {answer}")