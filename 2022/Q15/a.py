from collections import deque

from puzzle_input import input_data
from sample import sample_data


# data = sample_data.split("\n")
data = input_data.split('\n')

S = []

LIMIT = 4000000

V = set()

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

B = set()
S = []

for l in data:
    sInfo, bInfo = l.split(": ")
    
    sInfo = sInfo[10:]
    sx, sy = sInfo.split(", ")
    sx = int(sx[2:])
    sy = int(sy[2:])
    
    bInfo = bInfo[21:]
    bx, by = bInfo.split(", ")
    bx = int(bx[2:])
    by = int(by[2:])

    s = (sx,sy)
    b = (bx,by)
    d = distance(s,b)

    B.add(b)
    S.append( (s,b,d) )

T = [ [] for i in range(LIMIT+1) ]

for s,b,d in S:
    sx,sy = s
    for i in range(sy-d, sy+d+1):
        if i < 0 or i > LIMIT:
            continue
        r = abs(abs(sy-i) - d)
        start = max(0, sx-r)
        end = min(LIMIT, sx+r)
        T[i].append( (start, end+1) )

for i in range(LIMIT+1):
    T[i].sort()
    end = T[i][0][1]
    found = False
    for j in range(1, len(T[i])):
        ts,te = T[i][j]
        if ts > end:
            print('y=', i,'x=', end)
            found = True
            break
        end = max(end, te)
    if found:
        break
    # print('finished y=', i)


# for i in range(LIMIT+1):
#     for j in range(LIMIT+1):
#         found = False
#         for r in T[i]:
#             if j in range(*r):
#                 found = True
#                 break
#         if found:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print('')