with open('input.txt') as input_file:
    GRID = input_file.read().split('\n')

X, Y = range(2)
TRANSFORMS = {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)]
}


def getCharFromGrid(x, y):
    if x < 0 or x >= len(GRID[0]) or y < 0 or y >= len(GRID):
        return False
    return GRID[y][x]


def getConnections(char, pos):
    return [tuple([t[X] + pos[X], t[Y] + pos[Y]]) for t in TRANSFORMS[char]]


def getStartingChar(start_pos):
    for char in TRANSFORMS.keys():
        connections = getConnections(char, start_pos)
        start_found = True
        for connection in connections:
            connected_char = getCharFromGrid(*connection)
            if not connected_char or connected_char not in TRANSFORMS or start_pos not in getConnections(connected_char, connection):
                start_found = False
                break
        if start_found:
            return char


def generateLoop(start_char, start_pos):
    loop = set([start_pos])
    prev_pos = start_pos
    pos = getConnections(start_char, start_pos).pop()
    loop.add(pos)
    while pos != start_pos:
        char = getCharFromGrid(*pos)
        connections = getConnections(char, pos)
        connections.remove(prev_pos)
        prev_pos = pos
        pos = connections.pop()
        loop.add(pos)
    return loop


def isEnclosed(pos, loop):
    if pos in loop:
        return False
    current_pos = pos
    prev_edge = False
    edge_count = 0
    while True:
        current_pos = (current_pos[X] + 1, current_pos[Y])
        char = getCharFromGrid(*current_pos)
        if not char:
            break
        if current_pos in loop:
            if char == 'S':
                char = getStartingChar(current_pos)
            if char == '|':
                edge_count += 1
            elif (prev_edge == 'L' and char == '7') or (prev_edge == 'F' and char == 'J'):
                edge_count += 1
                prev_edge = False
        prev_edge = char if char == 'L' or char == 'F' else prev_edge
    if edge_count == 0:
        return False
    if edge_count % 2 != 0:
        return True
    return False


loop = set()
part1 = 0
for y, line in enumerate(GRID):
    if 'S' in line:
        x = line.index('S')
        loop = generateLoop(getStartingChar((x, y)), (x, y))
        part1 = int(len(loop) / 2)
        break

part2 = 0
for y, line in enumerate(GRID):
    for x, _ in enumerate(line):
        if isEnclosed((x, y), loop):
            part2 += 1

print('Part 1:', part1)
print('Part 2:', part2)
