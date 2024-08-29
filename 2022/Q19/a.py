# from collections import deque
# from functools import lru_cache
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
        (aOre, 0, 0, 0),
        (bOre, 0, 0, 0),
        (cOre, cClay, 0, 0),
        (dOre, 0, dObsidian, 0)
    ))

TIME_LIMIT = 24
M_LEN = 4
INIT_R = (1,0,0,0)
INIT_M = (0,0,0,0)
INTERATION_LIMIT = 50000000

sys.setrecursionlimit(INTERATION_LIMIT+100)

B = [0]
S = set()

BUFFER = [0]*M_LEN

def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(1, len(ss)+1)))

def canBuildRobot(rIds, materials):
    BUFFER = [0]*M_LEN
    for rId in rIds:
        for j in range(M_LEN):
            BUFFER[j] += BP[rId][j]
    for j in range(M_LEN):
        if materials[j] < BUFFER[j]:
            return False
    return True

def incrementRobot(rIds, robots):
    for i in range(M_LEN):
        BUFFER[i] = robots[i]
        if i in rIds:
            BUFFER[i] += 1
    return tuple(BUFFER)

def substractMaterials(rIds, materials):
    for i in range(M_LEN):
        BUFFER[i] = materials[i]
    for rId in rIds:
        for i in range(M_LEN):
            BUFFER[i] -= BP[rId][i]
    return tuple(BUFFER)

def mineMaterials(robots, materials):
    for i in range(M_LEN):
        BUFFER[i] = materials[i]
        BUFFER[i] += robots[i]
    return tuple(BUFFER)
    

def findBest(time, robots, materials):
    INT[0] += 1
    if time >= TIME_LIMIT:
        return

    S.add( (time, robots, materials) )

    # must create robot 3 if has enough materials
    tempR = tuple(robots)
    tempM = tuple(materials)
    lastRobot = [3]
    if canBuildRobot(lastRobot, tempM):
        tempR = incrementRobot(lastRobot, tempR)
        tempM = substractMaterials(lastRobot, tempM)
    
    # create robot cases
    subset = list(all_subsets([0, 1, 2]))
    random.shuffle(subset)
    for rIds in subset:
        if canBuildRobot(rIds, tempM):
            tr = incrementRobot(rIds, tempR)
            tm = substractMaterials(rIds, tempM)
            tm = mineMaterials(robots, tm)
            B[0] = max(B[0], tm[-1])
            if (time+1, tr, tm) not in S and INT[0] < INTERATION_LIMIT:
                findBest(time+1, tr, tm)
    
    tempM = mineMaterials(robots, tempM)
    B[0] = max(B[0], tempM[-1])
    # not creating any
    if (time+1, tempR, tempM) not in S and INT[0] < INTERATION_LIMIT:
        findBest(time+1, tempR, tempM)


ans = 0
for bpId in range(len(blueprints)):
    B = [0]
    S = set()
    INT = [0]
    BP = blueprints[bpId]
    findBest(0, INIT_R, INIT_M)
    ans += (bpId + 1) * B[0]
    print(bpId, B[0])
print(ans)