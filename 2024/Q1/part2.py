from my_input import sample_input
from my_input import my_input

from collections import Counter

def solve(input_s, debug = False):
    lines = input_s.split("\n")
    left = []
    right = []
    for line in lines:
        if line == '':
            break
        [a, b] = [ int(n) for n in line.split("   ") ]
        left.append(a)
        right.append(b)
    rightC = Counter(right)
    
    ans = 0
    for k in left:
        if k in rightC:
            ans += k * rightC[k]
    print(ans)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())