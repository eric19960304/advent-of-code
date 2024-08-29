from my_input import my_input

from collections import defaultdict
import sys
sys.setrecursionlimit(19600*2)

connectable = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['S', 'W'],
    'J': ['S', 'E'],
    '7': ['N', 'E'],
    'F': ['N', 'W']
}

connectTo = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['N', 'E'],
    'J': ['N', 'W'],
    '7': ['S', 'W'],
    'F': ['S', 'E']
}

corners = {
    'L': (-1, 1),
    'J': (-1, -1),
    '7': (1, -1),
    'F': (1, 1)
}

def getAdjs(grid, pos):
    M = len(grid)
    N = len(grid[0])
    y,x = pos
    currentPipe = grid[y][x]
    possibleAdjs = [(y+1, x, 'S'), (y-1, x, 'N'), (y, x+1, 'E'), (y, x-1, 'W')]
    possibleAdjs = list(filter(
        lambda x: 0 <= x[0] < M and 0 <= x[1] < N and (currentPipe == 'S' or x[2] in connectTo[currentPipe]), 
        possibleAdjs)
    )
    adjs = []
    for i,j,d in possibleAdjs:
        pipeType = grid[i][j]
        if pipeType in connectable and d in connectable[pipeType]:
            adjs.append((i,j))
    return adjs

def findCycle(G, V, pos, prev, isCycle):

    V.add(pos)
    M = len(G)
    N = len(G[0])

    adjs = getAdjs(G, pos)
    
    for a,b in adjs:
        if not (0 <= a < M and 0 <= b < N):
            continue
        if (a,b) != prev and (a,b) in V:
            isCycle.add(pos)
            continue
        if (a,b) in V:
            continue
        findCycle(G, V, (a,b), pos, isCycle)

def dfs(G, V, cyclePos, pos):
    V.add(pos)
    M = len(G)
    N = len(G[0])

    i,j = pos
    adjs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    
    for a,b in adjs:
        if not (0 <= a < M and 0 <= b < N):
            continue
        if (a,b) in cyclePos or (a,b) in V:
            continue
        dfs(G, V, cyclePos, (a,b))

def isAnyEnclosed(cycles, pos):
    for cycle in cycles:
        H = defaultdict(set)
        L = defaultdict(set)
        for a,b in cycle:
            H[a].add(b)
            L[b].add(a)
        y,x = pos
        hEnclosed = len([ n for n in H[y] if n < x]) %2 == 1 and len([ n for n in H[y] if n > x]) %2 == 1
        yEnclosed = len([ n for n in L[x] if n < y]) %2 == 1 and len([ n for n in L[x] if n > y]) %2 == 1
        if hEnclosed and yEnclosed:
            return True
    return False


def solve(input, debug = False):
    grid = input.split("\n")
    M = len(grid)
    N = len(grid[0])

    visited = set()
    cycles = []
    cycleV = set()
    for i in range(M):
        for j in range(N):
            if (i,j) not in visited and grid[i][j] != '.':
                V = set()
                isCycle = set()
                findCycle(grid, V, (i,j), None, isCycle)
                if len(isCycle) > 0:
                    cycles.append(V)
                    cycleV = cycleV | V
                visited = visited | V
    # if debug: print('nodes in cycles', len(cycleV))
    # if debug: print('number of cycles', len(cycles))
    
    inners = set()
    for y, x in cycleV:
        pipeType = grid[y][x]
        if pipeType in corners:
            dy, dx = corners[pipeType]
            a, b = y+dy, x+dx
            if (a,b) not in inners and (a,b) not in cycleV and 0 <= a < M and 0 <= b < N:
                dfs(grid, inners, cycleV, (a, b))
    result = 0
    for i in range(M):
        for j in range(N):
            if (i,j) in inners and (i,j) not in cycleV:
                result += 1
    print(result)

sample_input_1='''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
'''


sample_input_2='''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''

sample_input_3='''
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''

solve(sample_input_1.strip(), True)
solve(sample_input_2.strip(), True)
solve(sample_input_3.strip(), True)
print()
solve(my_input.strip(), False)
