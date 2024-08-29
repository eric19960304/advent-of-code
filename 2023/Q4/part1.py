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
    if debug: print("input size =", len(lines))
    points = 0
    for line in lines:
        numsHave, numsWin = parseInput(line)
        numsWinSet = set(numsWin)
        numsHaveSet = set(numsHave)
        commonSet = numsWinSet.intersection(numsHaveSet)
        if debug: print(commonSet)
        pointGot = int(2**(len(commonSet) - 1))
        if debug: print(commonSet, pointGot)
        points += pointGot
    print(points)


solve(sample_input.strip(), True)
print()
solve(my_input.strip())