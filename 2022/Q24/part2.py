from collections import deque
import heapq

from puzzle_input import input_data
from puzzle_sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

M = len(data)
N = len(data[0])

winds = {}
D = ['>', 'v', '<', '^']

w = set()
for i in range(M):
    for j in range(N):
        if data[i][j] == '#' or data[i][j] == '.':
            continue
        w.add( (i, j, data[i][j]) )
winds[0] = frozenset(w)

def simulateWinds(t):
    if t < 1:
        raise Exception('simulateWinds: invalid t')
    prevT = t-1
    if prevT not in winds:
        simulateWinds(prevT-1)
    
    nextW = set()
    prevW = winds[prevT]
    for y, x, d in prevW:
        newPos = None
        if d == '>':
            if x+1 == N - 1:
                newPos = (y, 1)
            else:
                newPos = (y, x+1)
        elif d == 'v':
            if y+1 == M - 1:
                newPos = (1, x)
            else:
                newPos = (y+1, x)
        elif d == '<':
            if x -1 == 0:
                newPos = (y, N - 2)
            else:
                newPos = (y, x-1)
        else: # ^
            if y - 1 == 0:
                newPos = (M-2, x)
            else:
                newPos = (y-1, x)
        ny, nx = newPos
        if data[ny][nx] == '#':
            raise Exception('hitting the wall')
        nextW.add( (ny, nx, d) )
    winds[t] = frozenset(nextW)


def isWind(y, x, t):
    if t not in winds:
        simulateWinds(t)
    
    isMatched = [ (y,x,d) in winds[t] for d in D ]
    return any(isMatched)

def calcDis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bfs(start, dest, initT):
    Q = [(calcDis(start, dest), start, initT)]
    foundCount = False

    V = set()
    ans = None
    while Q:
        _, u, t = heapq.heappop(Q)
        
        # print(c, t, calcDis(u, dest))
        
        y,x = u
        adjs = [(y+1, x),(y-1, x),(y, x+1),(y, x-1), (y, x)]
        adjs = list(filter(lambda x: 0 <=  x[0] < M and 0 <= x[1] <= N , adjs))
        
        for adj in adjs:
            if t+1 not in winds:
                simulateWinds(t+1)
            situation = (adj, winds[t+1])
            if situation in V:
                continue

            a,b = adj
            if data[a][b] == '#' or isWind(a, b, t+1):
                continue

            cost = t + 1 + calcDis(adj, dest)
            v = (cost, adj, t+1)

            if adj == dest:
                ans = v
                foundCount = True
                break
            V.add(situation)
            heapq.heappush(Q, v)
        if foundCount:
            break
    return ans
start = (0, 1)
goal = (M-1, N-2)
walk1 = bfs(start, goal, 0)
walk2 = bfs(goal, start, walk1[2])
walk3 = bfs(start, goal, walk2[2])
print(walk3)