from utils import input

input = input.text_to_string("3")

lines = input.split("\n")


def get_symbol_indexes():
    indexes = []
    for row, line in enumerate(lines):
        for column, char in enumerate(line):
            if not char.isdigit() and char != ".":
                indexes.append([column, row])

    return indexes


symbol_indexes = get_symbol_indexes()


def get_adjacent_indexes():
    indexes = []
    for start_index in symbol_indexes:
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
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
                numbers.append({
                    "value": int(current),
                    "indexes": [[x, row] for x in range(
                        start_index, end_index + 1)],
                    "is_symbol_adjacent": False})

    return numbers


numbers = find_numbers_with_indexes()


def find_part_numbers(numbers):
    part_numbers = []
    for number in numbers:
        for index in number["indexes"]:
            if index in symbol_adjacent_indexes:
                part_numbers.append(number["value"])
                break

    return part_numbers


part_numbers = find_part_numbers(numbers)

print(part_numbers)

answer = sum(part_numbers)

print(f"Solution: {answer}")
