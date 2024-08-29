from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = deque(sample_data.split("\n"))
data = deque(input_data.split('\n'))

F = {'size': 0, 'parent': None}
currentPath = F

while data:
    line = data.popleft()
    if line.startswith('$'):
        if 'cd' in line:
            commands = line.split(" ")
            directy = commands[-1]
            if directy == '..':
                currentPath = currentPath['parent']
            else:
                if currentPath and directy not in currentPath:
                    currentPath[directy] = {'size': 0, 'parent': currentPath}
                    currentPath = currentPath[directy]
        else:
            while data and not data[0].startswith('$'):
                file = data.popleft()
                if not file.startswith('dir'):
                    sizeInfo = file.split(" ")
                    currentPath['size'] += int(sizeInfo[0])
# print(F)

LIMIT = 100000
TOTAL = 70000000
REQUIRE = 30000000

cands = []
def traverse(root, ans):
    s = 0
    for k,v in root.items():
        if k == 'parent':
            continue
        if k == 'size':
            s += v
        else:
            s += traverse(root[k], ans)
    cands.append(s)
    return s

usedSize = traverse(F['/'], cands)
needAtLeast = REQUIRE - (TOTAL - usedSize)
ans = min(filter(lambda x: x >= needAtLeast, cands))
print(ans)