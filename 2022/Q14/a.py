from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

P = set()

maxX = 0
maxY = 0
minX = float('inf')

for lines in data:
    lines = lines.split(" -> ")
    for i in range(len(lines)-1):
        ax,ay = lines[i].split(",")
        bx,by = lines[i+1].split(",")
        ax,ay = int(ax), int(ay)
        bx,by = int(bx), int(by)
        if ax==bx:
            # horizontal line
            
            for y in range(min(ay, by), max(ay, by)+1):
                P.add( (ax, y) )
        elif ay==by:
            # vertical line
            for x in range(min(ax, bx), max(ax, bx)+1):
                P.add( (x, ay) )
        else:
            raise ValueError('unexpected input')

# print(P)

for x,y in P:
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    minX = min(minX, x)

print(maxX, maxY, minX)

for x in range(minX//2, maxX*2+1):
    P.add( (x, maxY+2) )

def moveSand(P, s):
    a,b = s
    fixed = False
    while True:
        adjs = [ (a,b+1), (a-1,b+1), (a+1,b+1)]
        adjs = list(filter(lambda x: x not in P, adjs))
        if len(adjs) == 0:
            P.add( (a,b) )
            # print('placed sand at ', a, b)
            fixed = True
            break
        for adj in adjs:
            a,b = adj
            break
    if not fixed:
        print("not fixed: ", a,b)
    return fixed

source = (500, 0)
S = []
count = 0
while True:
    s = (500, 0)
    if s in P:
        break
    moved = moveSand(P, s)
    # print(count, moved)
    if moved:
        count += 1
    else:
        break
print(count)