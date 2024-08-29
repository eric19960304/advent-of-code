from collections import deque

from puzzle_input import input_data
from sample import sample_data

data = sample_data.split("\n")
# data = input_data.split('\n')

ans = 0
for i in range(4, len(data)+1):
    prev = [int(x) for x in data[i-4:i-1]]
    current = [int(x) for x in data[i-3:i]]
    if prev and sum(current) > sum(prev):
        ans += 1
print(ans)