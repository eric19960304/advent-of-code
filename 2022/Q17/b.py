from collections import deque
import math
from puzzle_input import input_data
from sample import sample_data

# data = sample_data
data = input_data

TOP = -1
W = 7

def generateNextRock(i):
    Y = TOP + 4
    rocks = [
        [(2, Y), (3, Y), (4, Y), (5, Y)],
        [(2, Y+1), (3, Y), (3, Y+1), (3, Y+2), (4, Y+1)],
        [(2, Y), (3, Y), (4, Y), (4, Y+1),(4, Y+2)],
        [(2, Y), (2, Y+1), (2, Y+2), (2, Y+3)],
        [(2, Y), (3, Y), (2, Y+1), (3, Y+1)]
    ]
    return rocks[i%5]

def printCaveAndRock(top, CAVE, rock):
    for i in range(top, top - 5, -1):
        print('|', end='')
        for j in range(W):
            if (j,i) in CAVE:
                print('#', end='')
            elif (j,i) in rock:
                print('#',  end='')
            else:
                print('.', end='')
        print('|')
    print('+-------+')


target = 1000000000000
CAVE = set()
R = {}

gassCount = 0
rockCount = 0
while rockCount < target:
    # print('rockCount=', rockCount)

    rock = generateNextRock(rockCount)
    
    while True:
        # change by gas
        gasDir = data[gassCount%len(data)]
        gassCount += 1

        xDiff = -1 if gasDir == '<' else 1
        isValidMove = True
        for j in range(len(rock)):
            x,y = rock[j]
            newX = x+xDiff
            if newX < 0 or newX >= W or (newX, y) in CAVE:
                isValidMove = False
                break
        if isValidMove:
            for j in range(len(rock)):
                x,y = rock[j]
                rock[j] = (x+xDiff, y)

        # move down
        yDiff = -1
        isValidMove = True
        for j in range(len(rock)):
            x,y = rock[j]
            newY = y+yDiff
            if newY < 0 or (x,newY) in CAVE:
                isValidMove = False
                break
        if isValidMove:
            for j in range(len(rock)):
                x,y = rock[j]
                rock[j] = (x, y+yDiff)
        else:
            for r in rock:
                CAVE.add(r)
            break
    
    
    # update
    rockCount += 1
    for x,y in rock:
        TOP = max(TOP, y)

    # record the situation
    nearRocks = []
    for i in range(TOP, TOP-22, -1):
        for j in range(W):
            pair = (j, TOP - i)
            if (j, i) in CAVE:
                nearRocks.append(pair)
    
    situation = (frozenset(nearRocks), rockCount%5, gassCount%len(data))

    if situation in R:
        prevTop, prevRockCount = R[situation]
        diffTop = TOP - prevTop
        diffRockCount = rockCount - prevRockCount
        
        if diffRockCount + rockCount < target:
            # print('HIT', R[situation])
            rockCount = rockCount + diffRockCount
            TOP = TOP + diffTop
            newNearRock = []
            for a,b in nearRocks:
                p = (a, TOP - b)
                newNearRock.append(p)
                CAVE.add(p)
    R[situation] = (TOP, rockCount)

print(target, TOP+1)