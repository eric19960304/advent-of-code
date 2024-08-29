from my_input import sample_input
from my_input import my_input

from collections import Counter

def parseInput(line):
    left, rightNums = line.split("|")
    _, leftNums = left.split(":")
    numsHave = [ int(x) for x in leftNums.strip().split(" ") if len(x) > 0]
    numsWin = [ int(x) for x in rightNums.strip().split(" ") if len(x) > 0]
    return (numsHave, numsWin)

def solve(input, debug = False):
    lines = input.split("\n")
    N = len(lines)
    if debug: print("input size =", len(lines))
    wins = []
    cardCount = [1 for _ in range(N)]
    for line in lines:
        numsHave, numsWin = parseInput(line)
        numsWinSet = set(numsWin)
        numsHaveSet = set(numsHave)
        commonSet = numsWinSet.intersection(numsHaveSet)
        wins.append(len(commonSet))
    for i in range(N-1):
        for j in range(1, wins[i]+1):
            if i+j < N:
                cardCount[i+j] += cardCount[i]
    print(sum(cardCount))


solve(sample_input.strip(), True)
print()
solve(my_input.strip())