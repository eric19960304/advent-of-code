from collections import deque
import math

from puzzle_input import input_data
from puzzle_sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

MAP  = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

K = ['2', '1', '0', '-', '=']

def snafuToDecimal(s):
    ds = [c for c in s]
    i = 1
    ans = 0
    while len(ds) > 0:
        d = ds.pop()
        ans += MAP[d] * i
        i = i*5
    return ans

def decimalToSnafu(i):
    print(i, CONTEXT['n'])
    if CONTEXT['found']:
        return

    if CONTEXT['n'] == 0 and i==-1:
        print(CONTEXT['history'])
        CONTEXT['found'] = True
        return
    
    if i == -1:
        return
    
    choices = []
    for k in K:
        v = (5**i) * MAP[k]
        diff = abs(CONTEXT['n'] - v)
        choices.append( (diff, k, v) )
    choices.sort()

    for _, k, v in choices:
        CONTEXT['n'] -= v
        CONTEXT['history'].append(k)
        decimalToSnafu(i-1)
        if CONTEXT['found']:
            return
        CONTEXT['n'] += v
        CONTEXT['history'].pop()

s = 0
for d in data:
    s+= snafuToDecimal(d)
print(s)
CONTEXT = {
    'n': s,
    'found': False,
    'history': []
}
i = math.floor(math.log(s, 5))
decimalToSnafu(i)
ans = ''.join(CONTEXT['history'])
print(ans)
print(snafuToDecimal(ans))