from collections import Counter
import operator

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

P = set()
S = set()

minV = [float('inf'),float('inf'),float('inf')]
maxV = [0,0,0]

for l in data:
    val = [ int(x) for x in l.split(",") ]
    [x,y,z] = val
    P.add((x,y,z))
    for i in range(3):
        minV[i] = min(minV[i], val[i])
        maxV[i] = max(maxV[i], val[i])

G = Counter()
count = 0
for p in P:
    x,y,z = p
    adjs = [(x+1,y,z),(x,y+1,z),(x,y,z+1),(x-1,y,z),(x,y-1,z),(x,y,z-1)]
    for v in adjs:
        if v not in P:
            G[v] += 1
            count += 1

def inbound(t):
    for i in range(3):
        if t[i] < minV[i] or t[i] > maxV[i]:
            return False
    return True

for v in G:
    if v in P:
        continue
    isTrapped = True
    ds = [(1, 0, 0), (-1, 0, 0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    for d in ds:
        t = tuple(list(v))
        while inbound(t):
            t = tuple(map(operator.add, t, d))
            if t in P:
                break
        if t not in P:
            isTrapped = False
            break
    if isTrapped:
        count -= G[v]

print(count)
