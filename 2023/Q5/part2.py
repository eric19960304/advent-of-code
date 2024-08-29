from my_input import sample_input
from my_input import my_input

def isInSeeds(seedsRanges, num):
    for (start, end) in seedsRanges:
        if start <= num <= end:
            return True
    return False

def applyReverse(stepsRanges, i, x):
    if i < 0 or i >= len(stepsRanges):
        return x
    
    newX = x
    for (start, end), diff in stepsRanges[i]:
        if start <= newX <= end:
            newX += diff
            break
    return applyReverse(stepsRanges, i+1, newX)

def solve(input, debug = False):
    lines = input.split("\n\n")

    # parse input
    initSeedLine = lines[0]
    seeds = [ int(x) for x in initSeedLine.split(":")[1].strip().split(" ") ]
    seedsRanges = []
    maxSeed = 0
    for i in range(0, len(seeds), 2):
        seedsRanges.append((seeds[i], seeds[i] + seeds[i+1] - 1))
        maxSeed = max(maxSeed, seeds[i])
    
    stepsLines = lines[1:]
    stepsRanges = [ sl.split(":")[1].strip().split("\n") for sl in stepsLines]
    for i in range(len(stepsRanges)):
        stepsRanges[i] = [ [int(x) for x in r.split(" ") ] for r in stepsRanges[i] ]
    seedsRanges.sort()

    # construct steps
    for i in range(len(stepsRanges)):
        ranges = []
        for j in range(len(stepsRanges[i])):
            dest, source, l = stepsRanges[i][j]
            ranges.append((
                (dest, dest+l-1), 
                source - dest
            ))
        ranges.sort()
        stepsRanges[i] = ranges
    stepsRanges.reverse()
    if debug:
        print("seed ranges:", seedsRanges)
        print("step ranges:")
        for sr in stepsRanges:
            print(sr)
    
    for i in range(maxSeed):
        wantedSeed = applyReverse(stepsRanges, 0, i)
        if isInSeeds(seedsRanges, wantedSeed):
            print(i)
            break

solve(sample_input.strip(), True)
print()
solve(my_input.strip())