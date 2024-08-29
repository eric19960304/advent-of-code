from collections import deque
import functools

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n\n")
data = input_data.split('\n\n')

def compare(a, b):
    if type(a) is int and type(b) is int:
        return a - b
    elif type(a) is list and type(b) is list:
        for i in range(min(len(a), len(b))):
            c = compare( a[i], b[i] )
            if c != 0:
                return c
        return len(a) - len(b)
        
    elif type(a) is int and type(b) is list:
        return compare([a],b)
    elif type(a) is list and type(b) is int:
        return compare(a, [b])
    else:
        return 0
        

ans = 0
d1 = [[2]]
d2 = [[6]]
packets = [ d1, d2 ]
for i in range(len(data)):
    d = data[i]
    left, right = d.split("\n")
    left = eval(left)
    right = eval(right)
    packets.append(left)
    packets.append(right)
packets.sort(key=functools.cmp_to_key(compare))
ans = []
for i in range(len(packets)):
    if packets[i] == d1 or packets[i] == d2:
        ans.append(i+1)
print(ans[0]*ans[1])
