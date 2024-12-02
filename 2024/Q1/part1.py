from my_input import sample_input
from my_input import my_input

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
    left.sort()
    right.sort()
    ans = 0
    for i in range(len(left)):
        ans += abs(left[i] - right[i])
    print(ans)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())