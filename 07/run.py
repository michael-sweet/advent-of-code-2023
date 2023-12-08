from collections import Counter
from functools import cmp_to_key

with open('input.txt') as input_file:
    cards = [(line.split(' ')[0], int(line.split(' ')[1])) for line in input_file.read().split('\n')]

HIGHCARD, ONEPAIR, TWOPAIR, THREEKIND, FULLHOUSE, FOURKIND, FIVEKIND = range(1, 8)
cardvalues = {k: v for k, v in zip(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'], range(13, 0, -1))}
cardvalues_part2 = {k: v for k, v in zip(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'], range(13, 0, -1))}
part2 = False

def calculateType(hand):
    counter = Counter(hand)

    if part2 and 'J' in counter:
        j_count = counter['J']
        counter.subtract({'J': j_count})
        counter.update({counter.most_common(1)[0][0]: j_count})

    counts = counter.most_common()

    if counts[0][1] == 5:
        return FIVEKIND
    if counts[0][1] == 4:
        return FOURKIND
    if counts[0][1] == 3 and counts[1][1] == 2:
        return FULLHOUSE
    if counts[0][1] == 3:
        return THREEKIND
    if counts[0][1] == 2 and counts[1][1] == 2:
        return TWOPAIR
    if counts[0][1] == 2:
        return ONEPAIR

    return HIGHCARD


def compareByEachCard(card1, card2):
    for x in range(len(card1)):
        if cardvalues[card1[x]] > cardvalues[card2[x]]:
            return 1
        if cardvalues[card1[x]] < cardvalues[card2[x]]:
            return -1

    return 0


def sortCards(card1, card2):
    card1 = card1[0]
    card2 = card2[0]
    card1_type = calculateType(card1)
    card2_type = calculateType(card2)
    if card1_type > card2_type:
        return 1
    if card1_type < card2_type:
        return -1

    return compareByEachCard(card1, card2)


def calculateTotal():
    total = 0
    sorted_cards = sorted(cards, key=cmp_to_key(sortCards))
    for i, card in enumerate(sorted_cards):
        total += card[1] * (i + 1)

    return total


print('Part 1:', calculateTotal())

part2 = True
cardvalues = cardvalues_part2

print('Part 2:', calculateTotal())