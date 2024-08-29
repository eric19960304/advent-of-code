from my_input import sample_input
from my_input import my_input

from collections import deque
from collections import defaultdict

def solve(input_s, debug = False):
    grid = input_s.split("\n")
    
    M = len(grid)
    N = len(grid[0])

    start = None
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'S':
                start = (i,j)
                break
    
    stepOutMap = {}
    for y in range(M):
        for x in range(N):
            if grid[y][x] == '#':
                continue
            
            s = (y, x)
            Q = deque([(s, 0)])
            count = defaultdict(set)
            count[0].add(s)
            while Q:
                q, step = Q.pop()
                qi, qj = q

                if step >= 15:
                    continue

                adjs = [(qi+1, qj), (qi, qj+1), (qi-1, qj), (qi, qj-1)]
                for i,j in adjs:
                    if grid[i%M][j%N] == '#':
                        continue
                    if (i,j) in count[step+1]:
                        continue
                    Q.appendleft(( (i,j), step+1 ))
                    count[step+1].add((i,j))

            stepOutMap[s] = count[18]
    pos = set([start])
    step = 0
    ans = 0
    while step < 500:
        tempPos = set()
        for p in pos:
            ps = stepOutMap[p]
            ans += len(ps)
            for i,j in ps:
                if i >= M or j>=N:
                    tempPos.add((i%M,j%N))
        pos = tempPos
        step += 18
    print(step, ans)

solve(sample_input.strip(), True)
print()
# solve(my_input.strip())