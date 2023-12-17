from collections import Counter

with open('input.txt') as input_file:
    history_inputs = [[int(y) for y in x.split(' ')] for x in input_file.read().split('\n')]


def generateDifference(sequence):
    difference = []
    for i, value in enumerate(sequence):
        if i + 1 == len(sequence):
            return difference
        difference.append(sequence[i + 1] - value)


def generateDifferences(sequences):
    differences = [sequences]
    while Counter(differences[-1]).get(0, 0) != len(differences[-1]):
        differences.append(generateDifference(differences[-1]))
    return differences


def calculateNext(history):
    value = 0
    for difference in reversed(generateDifferences(history)):
        value += difference[-1]
    return value


def calculatePrev(history):
    value = 0
    for difference in reversed(generateDifferences(history)):
        value = difference[0] - value
    return value


part1 = part2 = 0
for history in history_inputs:
    part1 += calculateNext(history)
    part2 += calculatePrev(history)

print('Part 1:', part1)
print('Part 2:', part2)