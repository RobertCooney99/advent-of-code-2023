from utils import input

input = input.text_to_string("1")

lines = input.split("\n")

def accumulate(start_value, list, extractor, operation):
    result = start_value
    for item in list:
        result = operation(result, extractor(item))
    return result

def extract_number(line):
    digits = ''.join(char for char in line if char.isdigit())
    return int(digits[0] + digits[-1])

def add(a, b):
    return a + b

answer = accumulate(0, lines, extract_number, add)

print(f"Solution: {answer}")