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
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

scores = []

for line in data:
    S = []
    
    isCorrupted = False

    
    for c in line:
        if c in opens:
            S.append(c)
        else:
            if not S:
                isCorrupted = True
                break
            else:
                if S[-1] == brackets[c]:
                    S.pop()
                else:
                    isCorrupted = True
                    break
    
    if not isCorrupted:
        score = 0
        while S:
            s = S.pop()
            score *= 5
            score += errorScore[s]
        scores.append(score)
print(scores)
scores.sort()

ans = scores[len(scores)//2]
print(ans)
