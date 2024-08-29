from my_input import sample_input
from my_input import my_input

def applyStep(step, seed):
    for (start, end), diff in step:
        if start <= seed <= end:
            return seed + diff
    return seed

def solve(input, debug = False):
    lines = input.split("\n\n")

    # parse input
    initSeedLine = lines[0]
    seeds = [ int(x) for x in initSeedLine.split(":")[1].strip().split(" ") ]
    if debug: print(seeds)
    stepsLines = lines[1:]
    stepsRanges = [ sl.split(":")[1].strip().split("\n") for sl in stepsLines]
    for i in range(len(stepsRanges)):
        stepsRanges[i] = [ [int(x) for x in r.split(" ") ] for r in stepsRanges[i] ]
    if debug: print(stepsRanges[0], len(stepsRanges))
    
    # construct steps
    steps = []
    for i in range(len(stepsRanges)):
        transferRanges = []
        for j in range(len(stepsRanges[i])):
            dest, source, l = stepsRanges[i][j]
            transferRanges.append(
                ((source, source+l-1), dest - source)
            )
        steps.append(transferRanges)
    if debug: print(steps[0], len(steps))
    
    # apply steps to seeds
    for i in range(len(seeds)):
        for step in steps:
            seeds[i] = applyStep(step, seeds[i])

    print(min(seeds))

solve(sample_input.strip(), True)
print()
solve(my_input.strip())