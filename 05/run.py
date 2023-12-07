with open('input.txt') as input_file:
    input = input_file.read().split('\n\n')

DRS = 0 # destination range start
SRS = 1 # source range start
RL = 2 # range length

seeds = [int(x) for x in input[:1][0][len('seeds:'):].split()]
maps = {category.split(' map:')[0]: [tuple(int(v) for v in value.split()) for value in category.split(' map:\n')[1].split('\n')] for category in input[1:]}


def getMappedValueFromRange(lookup, ranges):
    for r in ranges:
        if lookup in range(r[SRS], r[SRS] + r[RL]):
            return r[DRS] + (lookup - r[SRS])
    return lookup


def traverseMaps(seed):
    result = {}
    lookup = seed
    for name, ranges in maps.items():
        result[name] = getMappedValueFromRange(lookup, ranges)
        lookup = result[name]

    return result


def getLowestLocation(seeds):
    lowest_location = float('inf')
    for seed in seeds:
        result = traverseMaps(seed)
        if result['humidity-to-location'] < lowest_location:
            lowest_location = result['humidity-to-location']
    return lowest_location


def getNextCategory(category):
    keys = list(maps.keys())
    key_pos = keys.index(category)
    if key_pos + 1 < len(keys):
        return keys[key_pos + 1]
    else:
        return None


def intersectRanges(source_range, map_ranges):
    intersects = []
    source_ranges = [source_range]
    for map_range in map_ranges:
        new_source_ranges = []
        for source_range in source_ranges:
            destination_range = (map_range[SRS], map_range[SRS] + map_range[RL] - 1)
            if source_range[1] < destination_range[0] or source_range[0] > destination_range[1]:
                new_source_ranges.append(source_range)
            else:
                intersect_start = source_range[0] if source_range[0] >= destination_range[0] else destination_range[0]
                intersect_end = source_range[1] if source_range[1] <= destination_range[1] else destination_range[1]
                if source_range[0] < destination_range[0]:
                    new_source_ranges.append((source_range[0], intersect_start))
                if source_range[1] > destination_range[1]:
                    new_source_ranges.append((intersect_end, source_range[1]))
                diff = map_range[DRS] - map_range[SRS]
                intersects.append((intersect_start + diff, intersect_end + diff))
        source_ranges = new_source_ranges

    intersects.extend(source_ranges)
    return intersects


def rangeLookup(lookup_ranges, category):
    all_matches = []
    for lookup_range in lookup_ranges:
        matches = intersectRanges(lookup_range, maps[category])
        all_matches.extend(matches)
    next_category = getNextCategory(category)
    if next_category:
        return rangeLookup(all_matches, next_category)

    return all_matches


part1 = getLowestLocation(seeds)

part2_seeds = []
seeds_copy = seeds.copy()
while len(seeds_copy) > 0:
    length = seeds_copy.pop()
    start = seeds_copy.pop()
    part2_seeds.append((start, start + length - 1))

part2 = min(rangeLookup(part2_seeds, 'seed-to-soil'))[0]

print('Part 1:', part1)
print('Part 2:', part2)
