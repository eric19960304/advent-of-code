from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

h = 0
d = 0
a = 0
for l in data:
    [c, n] = l.split(" ")
    n = int(n)

    if c == 'forward':
        h += n
        d += a * n
    elif c == 'up':
        a -= n
    else:
        a += n
print(h*d)