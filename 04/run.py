with open('input.txt') as input_file:
    input = input_file.read().split('\n')

games = [tuple(set(number.split()) for number in line.split(':')[1].split('|')) for line in input]


def getMatches(game):
    return game[0].intersection(game[1])


def calculateScore(match_count):
    if match_count == 0:
        return 0
    score = 1
    for x in range(1, match_count):
        score *= 2

    return score


part1 = 0
scratchcard_counts = {}
for i, game in enumerate(reversed(games)):
    match_count = len(getMatches(game))
    part1 += calculateScore(match_count)
    scratchcard_counts[i] = match_count
    for x in range(1, match_count + 1):
        scratchcard_counts[i] += scratchcard_counts[i - x]

part2 = sum(scratchcard_counts.values()) + len(games)


print('Part 1:', part1)
print('Part 2:', part2)