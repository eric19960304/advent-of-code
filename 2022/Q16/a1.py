from collections import deque
import heapq
from functools import lru_cache

from puzzle_input import input_data
from sample import sample_data

data = sample_data.split("\n")
# data = input_data.split('\n')

G = {}
F = {}
N = 0

for l in data:
    l1, l2 = l.split("; ")
    valve = l1[6:8]
    flow = int(l1.split("=")[1])
    l3 = l2.split("valve")[1]
    if l3[0] == 's':
        l3 = l3[1:]
    if l3[0] == ' ':
        l3 = l3[1:]
    adjs = l3.split(", ")
    
    F[valve] = flow
    G[valve] = adjs
    N += 1

# print(G)
# print(F)

V = set()

cands = []

@lru_cache
def visit(v, t, p, o, h):
    V.add( (v,t,p) )

    if t<=0 or len(o) == N:
        cands.append( (p, sorted(list(h))) )
        return

    for adj in G[v]:
        # open
        if F[adj] > 0 and adj not in o:
            newT = t-2
            newP = p + newT * F[adj]
            newO = o | frozenset([adj])
            newH = h | frozenset([(newT, adj)])
            if (adj, newT, newP) not in V:
                visit(adj, newT, newP, newO, newH)

        # not open
        if (adj, t-1, p) not in V:
            visit(adj, t-1, p, o, h)

visit('AA', 30, 0, frozenset('AA'), frozenset())
print(len(cands))
print(max(cands))
