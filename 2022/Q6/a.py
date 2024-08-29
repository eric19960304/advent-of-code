from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n\n")
data = input_data

W = 14
buffer = deque(data[:W])
i = W
while True:
    if len(set(buffer)) == len(buffer):
        break
    buffer.popleft()
    buffer.append(data[i])
    i += 1
print(i)