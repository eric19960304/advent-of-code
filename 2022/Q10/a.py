from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

N = len(data)
signal = []
value = 1
tasks = deque([None])
for line in data:
    if line == 'noop':
        tasks.append(None)
    else:
        [command, n] = line.split(" ")
        n = int(n)
        tasks.append(None)
        tasks.append(n)
while tasks:
    t = tasks.popleft()
    if t:
        value += t
    signal.append(value)
# print(signal)
ans = 0
for i in range(19, len(signal), 40):
    print(i, signal[i])
    ans += signal[i] * (i+1)

# print(signal)
CRT = ''
for i in range(1, len(signal)+1):
    inRange = [signal[i-1], signal[i-1]+1, signal[i-1]+2]
    if i%40 in inRange:
        print('#', end='')
    else:
        print('.', end='')
    if i in [40, 80, 120, 160, 200, 240]:
        print('')
# BPJAZGAP