from functools import reduce
from operator import mul

with open('input.txt') as input_file:
    input = input_file.read().split('\n')

part1_checks = {
    'red': 12,
    'green': 13,
    'blue': 14
}

part1 = 0
part2 = 0
for line in input:
    game_number = int(line.split(': ')[0][len('Game '):])
    part1_valid = True
    max_score = {}
    for round in line.split(': ')[1].split('; '):
        for colour_score in round.split(', '):
            score, colour = colour_score.split(' ')
            score = int(score)
            if score > part1_checks[colour]:
                part1_valid = False
            if max_score.get(colour, 0) < score:
                max_score[colour] = score
    if part1_valid:
        part1 += game_number
    part2 += reduce(mul, max_score.values())

print('Part 1:', part1)
print('Part 2:', part2)