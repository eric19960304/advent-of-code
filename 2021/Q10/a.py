from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

brackets = {')':'(', ']':'[', '}':'{', '>':'<'}

opens = brackets.values()
closes = brackets.keys()

print(closes, opens)

errorScore = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

errorCount = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
}

for line in data:
    S = []
    
    for c in line:
        if c in opens:
            S.append(c)
        else:
            if not S:
                errorCount[c] += 1
                # print(line)
                break
            else:
                if S[-1] == brackets[c]:
                    S.pop()
                else:
                    errorCount[c] += 1
                    # print(line)
                    break
ans = 0
for k in errorScore:
    ans += errorScore[k] * errorCount[k]
print(ans)
