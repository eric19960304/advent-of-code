from my_input import sample_input
from my_input import my_input
from collections import Counter

def getHandTypeRank(card):
    c = Counter(card)
    freq = list(c.values())
    maxRepeat = max(freq)
    if maxRepeat == 5:
        return 7
    elif maxRepeat == 4:
        return 6
    elif 3 in freq and 2 in freq:
        return 5
    elif maxRepeat == 3:
        return 4
    elif freq.count(2) == 2:
        return 3
    elif maxRepeat == 2:
        return 2
    else:
        return 1

def cardPower(card):
    powerMap = {
        'A': 50,
        'K': 40,
        'Q': 30,
        'J': 20,
        'T': 10,
    }
    return powerMap[card]

def getCardPowers(hand):
    return tuple([ int(x) if x.isnumeric() else cardPower(x) for x in hand ])

def getMaxCardRank(hand):
    return (getHandTypeRank(hand), tuple([ int(x) if x.isnumeric() else cardPower(x) for x in hand ]))

def solve(input, debug = False):
    lines = input.split("\n")
    cards = list(map(lambda x: x.split(" ")[0], lines))
    bids = list(map(lambda x: x.split(" ")[1], lines))
    if debug:
        print(cards, bids)
    ranks = []
    for i in range(len(cards)):
        r = getMaxCardRank(cards[i])
        ranks.append( (r, bids[i]) )
    ranks.sort()
    result = 0
    for i in range(len(ranks)):
        r, bid = ranks[i]
        if debug: print(r, bid, i+1)
        result += int(bid) * (i+1)
    print(result)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())