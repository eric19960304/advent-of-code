from my_input import sample_input
from my_input import my_input

def solve(input_s, debug = False):
    lines = input_s.split("\n")
    counter = 0
    for line in lines:
        nums = [int(n) for n in line.split(" ")]
        isSafe = False
        for j in range(len(nums)):
            newNums = [ nums[k] for k in range(len(nums)) if k != j ]

            diffs = []
            for i in range(len(newNums)-1):
                diffs.append(newNums[i+1] - newNums[i])
            absDiffs = [ abs(d) for d in diffs ]
            if any([ d < 1 or d > 3 for d in absDiffs ]):
                continue
            if not (all([ d > 0 for d in diffs ]) or all([ d < 0 for d in diffs ])):
                continue
            isSafe = True
            break
        if isSafe:
            counter += 1
    print(counter)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())