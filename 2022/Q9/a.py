from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

hPos = (0,0)
tPos = [(0,0) for i in range(9)]

V = set()
V.add((0,0))

dirMap = {'R': (1,0), 'L': (-1, 0), 'U': (0, 1), 'D': (0,-1)}

for line in data:
    [direction, move] = line.split(" ")
    
    move = int(move)
    
    dd = dirMap[direction]

    for i in range(move):
        hPos = (hPos[0] + dd[0], hPos[1] + dd[1])

        for j in range(9):
            succ = tPos[j-1] if j > 0 else hPos
            if abs(succ[0] - tPos[j][0]) >= 2:
                sD = succ[1] - tPos[j][1]
                if sD != 0:
                    sD = sD//abs(sD)
                newX = succ[0] - 1 if tPos[j][0] < succ[0] else succ[0] + 1
                newY = tPos[j][1] + sD
                tPos[j] = (newX, newY)
            elif abs(succ[1] - tPos[j][1]) >= 2:
                sD = succ[0] - tPos[j][0]
                if sD != 0:
                    sD = sD//abs(sD)
                newX = tPos[j][0] + sD
                newY = succ[1] - 1 if tPos[j][1] < succ[1] else succ[1] + 1
                tPos[j] = (newX, newY)
        
            V.add(tPos[-1])
    print(hPos, tPos)

print(len(V))
