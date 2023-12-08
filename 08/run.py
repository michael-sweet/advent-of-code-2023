import math

with open('input.txt') as input_file:
    instructions, nodes = input_file.read().split('\n\n')
nodes = {node.split(' = ')[0]: tuple(node.split(' = ')[1].strip('()').split(', ')) for node in nodes.split('\n')}

DIRECTION = {'L': 0, 'R': 1}


def part1():
    steps = 0
    current_node = 'AAA'
    while True:
        for instruction in instructions:
            current_node = nodes[current_node][DIRECTION[instruction]]
            steps += 1
            if current_node == 'ZZZ':
                return steps


print('Part 1:', part1())


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcmList(list):
    result = list.pop()
    for x in list:
        result = lcm(result, x)

    return result


cycle_steps = []
current_nodes = [node for node in nodes.keys() if node[2] == 'A']
for i, current_node in enumerate(current_nodes):
    steps = 0
    while current_node[2] != 'Z':
        for instruction in instructions:
            steps += 1
            current_node = nodes[current_node][DIRECTION[instruction]]
            if current_node[2] == 'Z':
                break
    cycle_steps.append(steps)

print('Part 2:', lcmList(cycle_steps))