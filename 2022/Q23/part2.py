from collections import deque
from collections import Counter

from puzzle_input import input_data
from puzzle_sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

G = set()
M = len(data)
N = len(data[0])
print(M, N)

def printG(y1, x1, y2, x2):
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if (i,j) in G:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

for i in range(M):
    for j in range(N):
        if data[i][j] == '#':
            G.add((i,j))

checkLists = deque([
    [(-1, 0), (-1, -1), (-1, 1)], # N
    [(1, 0), (1, -1), (1, 1)], # S
    [(0, -1), (-1, -1), (1, -1)], # W
    [(0, 1), (-1, 1), (1, 1)] # E
])

def findEmptyAdjs(p):
    adjs = []
    for cl in checkLists:
        hasEmptyAdj = True
        for dy, dx in cl:
            checkP = (p[0]+dy, p[1]+dx)
            if checkP in G:
                hasEmptyAdj = False
                break
        if hasEmptyAdj:
            dy, dx = cl[0]
            adjs.append( (p[0]+dy, p[1]+dx) )
    return adjs

roundCount = 0
while True:
    moved = False
    # propose the move
    proposal = {}
    proposed = Counter()
    for p in G:
        proposal[p] = findEmptyAdjs(p)
        if len(proposal[p]) != 4 and len(proposal[p]) != 0:
            proposed[proposal[p][0]] += 1
    # print(proposal)

    # move
    for p in proposal:
        if len(proposal[p]) == 4 or len(proposal[p])==0:
            continue
        newP = proposal[p][0]
        if newP not in G and (newP in proposed and proposed[newP] == 1):
            G.remove(p)
            G.add(newP)
            moved = True
    
    # update checkLists
    checkLists.append(checkLists.popleft())

    # printG(0, 0, M-1, N-1)

    roundCount += 1
    if not moved:
        break

borders = [float('inf'), float('inf'), 0, 0]
for p in G:
    py, px = p
    y1, x1, y2, x2 = borders
    borders = [
        min(y1, py),
        min(x1, px),
        max(y2, py),
        max(x2, px)
    ]
y1, x1, y2, x2 = borders
# printG(y1, x1, y2, x2)
# ans = (y2 - y1 + 1) * (x2 - x1 +1) - len(G)
# print(ans)
print(roundCount)