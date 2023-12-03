from utils import input

input = input.text_to_string("1")

lines = input.split("\n")

def accumulate(start_value, list, extractor, operation):
    result = start_value
    for item in list:
        result = operation(result, extractor(item))
    return result

def replace_word_with_number(line):
    numbers_as_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    did_replace = False

    for index, char in enumerate(line):
        if not char.isdigit():
            for int_value, number in enumerate(numbers_as_words, 1):
                if line[index : index + len(number)] == number:
                    did_replace = True
                    line = line[:index] + str(int_value) + line[index+len(number):]
                    break

    return line, did_replace

def extract_number(line):
    while True:
        line, did_replace = replace_word_with_number(line)
        if not did_replace:
            break

    digits = ''.join(char for char in line if char.isdigit())
    return int(digits[0] + digits[-1])

def add(a, b):
    return a + b

answer = accumulate(0, lines, extract_number, add)

print(f"Solution: {answer}")