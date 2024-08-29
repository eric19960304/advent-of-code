from my_input import sample_input
from my_input import my_input

def factorial(x):
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def arrangementR(slots, nums):
    # impossible case
    slotLenSum = [ len(x) for x in slots ]
    validSpring = sum(nums)
    if slotLenSum < validSpring:
        return 0
    
    result = 0
    return 0

def findArrangements(line):
    [symbols, nums] = line.split(" ")
    nums = [ int(x) for x in nums.split(",") ]
    segments = []
    prev = []
    for s in symbols:
        if s == '.':
            if prev:
                segments.append("".join(prev))
            prev = []
        else:
            prev.append(s)
    if prev:
        segments.append("".join(prev))
    print('segments', segments)
    print('nums', nums)

    slots = [ (len(segment), segment[0] == '?') for segment in segments if len(segment) > 0]

    result = 0
    result += arrangementR(slots, nums)
    return result

def solve(input, debug = False):
    lines = input.split("\n")
    result = 0
    for line in lines:
        result += findArrangements(line)
    print(result)
    

solve(sample_input.strip(), True)
print()
# solve(my_input.strip())