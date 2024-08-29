from collections import deque

from puzzle_input import input_data
from sample import sample_data

data = sample_data
# data = input_data

# print(len(data))

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

def printCaveAndRock(CAVE, rock):
    for i in range(TOP, -1, -1):
        print('|', end='')
        for j in range(W):
            if (j,i) in CAVE:
                print('#', end='')
            elif (j,i) in rock:
                print('#')
            else:
                print('.', end='')
        print('|')
    print('+-------+')

CAVE = set()
gasIdx = 0
for i in range(2022):
    # print(i)
    rock = generateNextRock(i)
    
    while True:
        # change by gas
        gasDir = data[gasIdx%len(data)]
        gasIdx += 1
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
        
        # printCaveAndRock(CAVE, rock)

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
        # printCaveAndRock(CAVE, rock)
    # print(rock, CAVE)

    for x,y in rock:
        TOP = max(TOP, y)
    # print('i=', i, ', max TOP=', TOP)
# printCaveAndRock(CAVE, [])
print(TOP+1)