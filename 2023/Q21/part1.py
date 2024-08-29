from my_input import sample_input
from my_input import my_input

from collections import deque
from collections import defaultdict

def solve(input, debug = False):
    grid = input.split("\n")
    
    M = len(grid)
    N = len(grid[0])

    s = None
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'S':
                s = (i,j)

    Q = deque([(s, 0)])
    count = defaultdict(set)
    count[0].add(s)
    limit = 64
    while Q:
        q, step = Q.pop()
        qi, qj = q

        if step >= limit:
            continue

        adjs = [(qi+1, qj), (qi, qj+1), (qi-1, qj), (qi, qj-1)]
        for i,j in adjs:
            if grid[i%M][j%N] == '#':
                continue
            if (i,j) in count[step+1]:
                continue
            Q.appendleft(( (i,j), step+1 ))
            count[step+1].add((i,j))
    print(len(count[limit]))

solve(sample_input.strip(), True)
print()
# solve(my_input.strip())