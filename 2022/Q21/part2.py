from collections import deque

from puzzle_input import input_data
from puzzle_sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

G = {}
for line in data:
    name, ops = line.split(": ")
    if ops.isdigit():
        G[name] = (int(ops),)
    else:
        m1, op, m2 = ops.split(" ")
        G[name] = (op, m1, m2)
HUMAN_VAL = [0]
def dfs(name):
    if name == 'humn':
        return HUMAN_VAL[0]

    if len(G[name]) == 1:
        return G[name][0]
    else:
        op, m1, m2 = G[name]
        v1 = dfs(m1)
        v2 = dfs(m2)
        if op == '+':
            return v1 + v2
        elif op == '-':
            return v1 - v2
        elif op == '*':
            return v1 * v2
        else: # /
            return v1 // v2


def calcDiff(human_val):
    HUMAN_VAL[0] = human_val
    _, m1, m2 = G['root']
    v1 = dfs(m1)
    v2 = dfs(m2)
    return v1 - v2


def findHumanVal():
    # real input
    l = 100000
    r = 1000000000000000000

    # sameple
    # l = 5
    # r = 400

    while l <= r:
        m = l + (r-l)//2
        v = calcDiff(m)
        print(m, v)
        if v == 0:
            return m
        elif v > 0:
            l = m + 1
        else:
            r = m - 1
    return l

HUMAN_VAL[0] = findHumanVal()
_, m1, m2 = G['root']
v1 = dfs(m1)
v2 = dfs(m2)
print(HUMAN_VAL[0], v1, v2)
