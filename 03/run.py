import re

with open('input.txt') as input_file:
    input = input_file.read().split('\n')


def isSymbol(value):
    return bool(re.match('[^\d|\.]', value))


def isGear(value):
    return value == '*'


def checkAdjacent(x, y):
    has_symbol = False
    has_gear = False
    for a, b in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        check_x = x + a
        check_y = y + b
        if (
            check_x >= 0 and check_x < len(input[0]) and
            check_y >= 0 and check_y < len(input)
        ):
            value = input[check_y][check_x]
            if isSymbol(value):
                has_symbol = True
            if isGear(value):
                has_gear = (check_x, check_y)

    return (has_symbol, has_gear)


part1 = 0
potential_gears = {}
for y, line in enumerate(input):
    result = re.finditer('\d+', line)
    for match in result:
        symbol_found = False
        gear_found = False
        number = int(match.group())
        for x in range(match.span()[0], match.span()[1]):
            has_symbol, gear = checkAdjacent(x, y)
            if not symbol_found and has_symbol:
                part1 += number
                symbol_found = True
            if not gear_found and gear:
                if gear not in potential_gears:
                    potential_gears[gear] = []
                potential_gears[gear].append(number)
                gear_found = True

part2 = 0
for gear_ratios in potential_gears.values():
    if len(gear_ratios) == 2:
        part2 += gear_ratios[0] * gear_ratios[1]


print('Part 1:', part1)
print('Part 2:', part2)