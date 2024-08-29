from collections import deque
import math

from puzzle_input import input_data
from puzzle_sample import sample_data

# map, moves = sample_data.split("\n\n")
map, moves = input_data.split('\n\n')

G = map.split("\n")

M = len(G)
N = len(G[0])

for i in range(len(G)):
    N = max(N, len(G[i]))
print('M=', M)
print('N=', N)

H1 = [float('inf')] * M
H2 = [0] * M
V1 = [float('inf')] * N
V2 = [0] * N

walls = set()

FN = {
    (0,1): 1,
    (0,2): 2,
    (1,1): 3,
    (2,0): 4,
    (2,1): 5,
    (3,0): 6
}

tops = [[] for i in range(6)]
bottoms = [[] for i in range(6)]
lefts = [[] for i in range(6)]
rights = [[] for i in range(6)]

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

facingScore = {
    '>': 0,
    'v': 1,
    '<': 2,
    '^': 3
}

HM = {}
VM = {}

C = int(math.sqrt((M*N)//12))
print('C=', C)

for i in range(M):
    for j in range(len(G[i])):
        if G[i][j] == '#':
            walls.add((i,j))
        if G[i][j] == '.' or G[i][j] == '#':
            H1[i] = min(H1[i], j)
            H2[i] = max(H2[i], j)
            V1[j] = min(V1[j], i)
            V2[j] = max(V2[j], i)
        cPos = (i//C, j//C)
        if cPos in FN:
            number = FN[cPos] - 1
            if i%C == 0:
                tops[number].append( (i,j) )
            if i%C == C-1:
                bottoms[number].append( (i,j) )
            if j%C == 0:
                lefts[number].append( (i,j) )
            if j%C == C-1:
                rights[number].append( (i,j) )

def createHM(a, b, d):
    for i in range(len(a)):
        HM[a[i]] = (b[i][0], b[i][1], d)
def createVM(a, b, d):
    for i in range(len(a)):
        VM[a[i]] = (b[i][0], b[i][1], d)

createVM(tops[0], lefts[5], '>')
createHM(lefts[0], list(reversed(lefts[3])), '>')

createVM(tops[1], bottoms[5], '^')
createVM(bottoms[1], rights[2], '<')
createHM(rights[1], list(reversed(rights[4])), '<')

createHM(lefts[2], tops[3], 'v')
createHM(rights[2], bottoms[1], '^')

createVM(tops[3], lefts[2], '>')
createHM(lefts[3], list(reversed(lefts[0])), '>')

createVM(bottoms[4], rights[5], '<')
createHM(rights[4], list(reversed(rights[1])), '<')

createVM(bottoms[5], tops[1], 'v')
createHM(lefts[5], tops[0], 'v')
createHM(rights[5], bottoms[4], '^')

print(len(VM), len(HM))

def isWall(y, x):
    return (y, x) in walls

def move(p, d, f):
    newF = f
    while d > 0:
        y,x = p
        # print(p)
        if f == '>':
            newY = HM[p][0] if x == H2[y] else y
            newX = HM[p][1] if x == H2[y] else x+1
            if x == H2[y]:
                newF = HM[p][2]
        elif f == 'v':
            newY = VM[p][0] if y == V2[x] else y+1
            newX = VM[p][1] if y == V2[x] else x
            if y == V2[x]:
                newF = VM[p][2]
        elif f == '<':
            newY = HM[p][0] if x == H1[y] else y
            newX = HM[p][1] if x == H1[y] else x-1
            if x == H1[y]:
                newF = HM[p][2]
        else: # ^
            newY = VM[p][0] if y == V1[x] else y-1
            newX = VM[p][1] if y == V1[x] else x
            if y == V1[x]:
                newF = VM[p][2]
        if isWall(newY, newX):
            break
        p = (newY, newX)
        d -= 1
    return p,newF

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
        pos, facing = move(pos, distance, facing)
    else:
        direction = moves[i]
        if direction == 'L':
            facing = leftTurn[facing]
        else:
            facing = rightTurn[facing]
        i += 1


print(pos[0] + 1, pos[1] + 1, facing)
score = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + facingScore[facing]
print(score)