from my_input import my_input

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

def solve(input, debug = False):
    grid = input.split("\n")
    M = len(grid)
    N = len(grid[0])
    startPos = None
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'S':
                startPos = (i, j)
                break
        if startPos != None:
            break
    if debug: print(startPos)

    count = 1
    prevP1, prevP2 = startPos, startPos
    [p1, p2] = getAdjs(grid, startPos)
    while p1 != p2:
        if debug: print(p1, p2, grid[p1[0]][p1[1]], grid[p2[0]][p2[1]])
        newP1 = list(filter(lambda x: x != prevP1, getAdjs(grid, p1)))[0]
        newP2 = list(filter(lambda x: x != prevP2, getAdjs(grid, p2)))[0]
        prevP1 = p1
        prevP2 = p2
        p1 = newP1
        p2 = newP2
        count += 1
    print(count)
        
sample_input_1='''
.....
.S-7.
.|.|.
.L-J.
.....
'''

sample_input_2='''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''


solve(sample_input_1.strip(), True)
print()
solve(sample_input_2.strip(), True)
print()
solve(my_input.strip(), True)
