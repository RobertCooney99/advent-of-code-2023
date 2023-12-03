from utils import input

input = input.text_to_string("3")

lines = input.split("\n")

def get_symbol_indexes():
    indexes = []
    gear_indexes = []
    for row, line in enumerate(lines):
        for column, char in enumerate(line):
            if not char.isdigit() and char != ".":
                if char == "*":
                    gear_indexes.append([column, row])
                indexes.append([column, row])
    
    return indexes, gear_indexes

symbol_indexes, gear_indexes = get_symbol_indexes()

def get_adjacent_indexes():
    indexes = []
    for start_index in symbol_indexes:
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0: continue
                adjacent_index = [start_index[0] + x, start_index[1] + y]
                if adjacent_index[0] >= 0 and adjacent_index[1] >= 0:
                    indexes.append(adjacent_index)

    return indexes

def deduplicate_indexes(indexes):
    index_set = set(tuple(i) for i in indexes)
    return [list(x) for x in index_set]

symbol_adjacent_indexes = deduplicate_indexes(get_adjacent_indexes())

def find_numbers_with_indexes():
    numbers = []
    for row, line in enumerate(lines):
        index = 0
        while index < len(line):
            start_index = index
            current = ""

            while index < len(line) and line[index].isdigit():
                current += line[index]
                index += 1
            
            end_index = index - 1
            index += 1

            if len(current) > 0:
                numbers.append({"value": int(current), "indexes": [[x, row] for x in range(start_index, end_index + 1)], "is_symbol_adjacent": False})

    return numbers

numbers = find_numbers_with_indexes()

def find_part_numbers(numbers):
    part_numbers = []
    for number in numbers:
        for index in number["indexes"]:
            if index in symbol_adjacent_indexes:
                part_numbers.append(number)
                break

    return part_numbers

part_numbers = find_part_numbers(numbers)

def find_gear_ratios(part_numbers, gear_indexes):
    ratios = []

    for gear_index in gear_indexes:
        adjacent_part_number_values = []
        for part_number in part_numbers:
            is_part_number_adjacent = False
            for index in part_number["indexes"]:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0: continue
                        if (index == [gear_index[0] + x, gear_index[1] + y]):
                            is_part_number_adjacent = True
            if is_part_number_adjacent:
                adjacent_part_number_values.append(part_number["value"])

        if len(adjacent_part_number_values) == 2:
            ratios.append(adjacent_part_number_values[0] * adjacent_part_number_values[1])

    return ratios

gear_ratios = find_gear_ratios(part_numbers, gear_indexes)

answer = sum(gear_ratios)

print(f"Solution: {answer}")