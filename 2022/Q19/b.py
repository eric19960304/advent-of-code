from collections import deque
from functools import lru_cache
from itertools import chain, combinations
import sys
import random

from puzzle_input import input_data
from sample import sample_data

data = sample_data.split("\n")
# data = input_data.split('\n')

# costs of [ore, clay, obsidian, geode] robots
# materials (ore, clay, obsidian)
blueprints = []
for line in data:
    [a, b, c, d] = line.split(": ")[1].split(". ")
    a = a.split("costs ")[1]
    aOre = int(a[:-4])
    
    b = b.split("costs ")[1]
    bOre = int(b[:-4])

    c = c.split("costs ")[1]
    cOre, cClay = c.split(" ore and ")
    cOre = int(cOre)
    cClay = int(cClay[:-5])

    d = d.split("costs ")[1]
    dOre, dObsidian = d.split(" ore and ")
    dOre = int(dOre)
    dObsidian = int(dObsidian[:-9])

    blueprints.append((
        (aOre, 0, 0, 0), # ore
        (bOre, 0, 0, 0), # clay
        (cOre, cClay, 0, 0), # obsidian 
        (dOre, 0, dObsidian, 0) # geode
    ))

TIME_LIMIT = 24
M = 4
INIT_R = (1,0,0,0)
INIT_M = (0,0,0,0)

for blueprint in blueprints:

    print('blueprint')
    for i in range(len(blueprint)):
        print(blueprint[i])
    print()

    target = [0]*M
    dp = [ [0]*M for i in range(M) ]

    print('dp')
    for i in range(M):
        dp[0][i] += blueprint[0][i]

    for i in range(1, M):
        quant = blueprint[i]
        dp[i][0] += quant[0]

        for j in range(1, M):
            q = quant[j]
            for k in range(M):
                dp[i][j] += q * dp[j][k]
    for i in range(M):
        print(dp[i])
    print()

    for i in range(M):
        for j in range(M):
            target[i] += dp[j][i]
    print('target', target)
    print('-----------------------------')