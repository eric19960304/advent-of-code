from collections import deque

from puzzle_input import input_data
from puzzle_sample import sample_data

map, moves = sample_data.split("\n\n")
# map, moves = input_data.split('\n\n')

G = map.split("\n")

M = len(G)
N = len(G[0])

for i in range(len(G)):
    N = max(N, len(G[i]))
print(M, N)

H1 = [float('inf')] * M
H2 = [0] * M
V1 = [float('inf')] * N
V2 = [0] * N

walls = set()

for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j] == '#':
            walls.add((i,j))
        if G[i][j] == '.' or G[i][j] == '#':
            H1[i] = min(H1[i], j)
            H2[i] = max(H2[i], j)
            V1[j] = min(V1[j], i)
            V2[j] = max(V2[j], i)

# print(len(H1))
# print(len(H2))
# print(len(V1))
# print(len(V2))

leftTurn = {
    '>': '^',
    'v': '>',
    '<': 'v',
    '^': '<'
}

rightTurn = {
    '>': 'v',
    'v': '<',
    '<': '^',
    '^': '>'
}

def isWall(y, x):
    return (y, x) in walls

def move(p, d, f):
    while d > 0:
        y,x = p
        # print(p)
        if f == '>':
            newX = H1[y] if x == H2[y] else x+1
            if isWall(y, newX):
                break
            p = (y, newX)
        elif f == 'v':
            newY = V1[x] if y == V2[x] else y+1
            if isWall(newY, x):
                break
            p = (newY, x)
        elif f == '<':
            newX = H2[y] if x == H1[y] else x-1
            if isWall(y, newX):
                break
            p = (y, newX)
        else: # ^
            newY = V2[x] if y == V1[x] else y-1
            if isWall(newY, x):
                break
            p = (newY, x)
        d -= 1
    return p

i = 0
facing = '>'
pos = (0, H1[0])
while i < len(moves):
    if moves[i].isdigit():
        distance = []
        while i < len(moves) and moves[i].isdigit():
            distance.append(moves[i])
            i+=1
        distance = int(''.join(distance))
        pos = move(pos, distance, facing)
    else:
        direction = moves[i]
        if direction == 'L':
            facing = leftTurn[facing]
        else:
            facing = rightTurn[facing]
        i += 1


facingScore = {
    '>': 0,
    'v': 1,
    '<': 2,
    '^': 3
}

print(pos[0] + 1, pos[1] + 1, facing)
score = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + facingScore[facing]
print(score)