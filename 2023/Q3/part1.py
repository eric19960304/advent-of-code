from my_input import sample_input
from my_input import my_input

def getAdjNumbersSum(grid, pos, visited, debug = False):
    pi, pj = pos
    adjs = [(pi+1, pj), (pi-1, pj), (pi, pj+1), (pi, pj-1), (pi+1, pj+1), (pi-1, pj-1), (pi+1, pj-1), (pi-1, pj+1)]
    numbers = []
    for i,j in adjs:
        if isInBound(grid, (i,j)) and grid[i][j].isnumeric() and (i,j) not in visited:
            numPos = []
            numPos.append((i,j))
            y,x = i,j-1
            # move left
            while isInBound(grid, (y,x)) and grid[y][x].isnumeric():
                numPos.append((y,x))
                visited.add((y,x))
                x -= 1
            # move right
            y,x = i, j+1
            while isInBound(grid, (y,x)) and grid[y][x].isnumeric():
                numPos.append((y,x))
                visited.add((y,x))
                x += 1
            numPos.sort()
            numbers.append(int("".join([ grid[a][b] for a,b in numPos])))
    if debug: print(numbers)
    return sum(numbers)

def isInBound(grid, pos):
    M = len(grid)
    N = len(grid[0])
    i, j = pos
    return 0 <= i < M and 0 <= j < N

def solve(input, debug = False):
    grid = input.split("\n")
    M = len(grid)
    N = len(grid[0])
    if debug: print("M=%d, N=%d".format(M, N))
    symbols = []
    for i in range(M):
        for j in range(N):
            if not grid[i][j].isnumeric() and grid[i][j] != '.':
                symbols.append((i,j))
    if debug: print(symbols)
    if debug: print("len(symbols)", len(symbols))

    visited = set()
    result = 0
    for symbol in symbols:
        result += getAdjNumbersSum(grid, symbol, visited, debug)
    print(result)
    

solve(sample_input.strip(), True)
print()
solve(my_input.strip())