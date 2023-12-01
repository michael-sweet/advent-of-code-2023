import re

with open('input.txt') as input_file:
    input = input_file.read().split('\n')


def isNumber(x) -> bool:
    try:
        int(x)
        return True
    except:
        return False


def calculateValue(input:list):
    values = [[char for char in line if isNumber(char)] for line in input]
    values = [int(''.join([value[0], value[-1]])) for value in values]

    return sum(values)


def replaceAllFancyNumbers(line:str):
    lookup = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }

    def replaceFancyNumber(possible_number):
        return lookup[possible_number.group()]

    pattern = '|'.join(lookup.keys())
    while True:
        new_line = re.sub(pattern, replaceFancyNumber, line)
        if line == new_line:
            return new_line
        line = new_line


part2_input = [replaceAllFancyNumbers(line) for line in input]

print('Part 1:', calculateValue(input))
print('Part 2:', calculateValue(part2_input))
