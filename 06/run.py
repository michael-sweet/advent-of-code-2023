with open('input.txt') as input_file:
    input = input_file.read().split('\n')

times = [int(x) for x in input[0][len('Time:'):].split()]
distances = [int(x) for x in input[1][len('Distance:'):].split()]


def calculateTotalWinners(times, distances):
    total_score = 1
    for i, time in enumerate(times):
        score = time + 1
        for x in range(time + 1):
            if x * (time - x) > distances[i]:
                score -= x
                break
        for x in range(time + 1, 0, -1):
            if x * (time - x) > distances[i]:
                score -= time - x
                break
        total_score *= score

    return total_score


print('Part 1:', calculateTotalWinners(times, distances))

times = [int(input[0][len('Time:'):].replace(' ', ''))]
distances = [int(input[1][len('Distance:'):].replace(' ', ''))]

print('Part 2:', calculateTotalWinners(times, distances))