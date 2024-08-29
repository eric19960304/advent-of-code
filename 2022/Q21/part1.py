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

def dfs(name):
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

print(dfs('root'))