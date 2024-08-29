from puzzle_input import input_data
from puzzle_sample import sample_data

from collections import deque

data = sample_data.split("\n")
# data = input_data.split('\n')

P = {}
R = {}
N = len(data)
order = []
zeroId = None

for i in range(N):
    d = int(data[i])
    d *= 811589153
    P[i] = (d,i)
    R[i] = i
    order.append(i)
    if d == 0:
        zeroId = i

for t in range(10):
    for i in range(len(order)):
        d = order[i]
        if d == zeroId:
            continue

        currentPos = R[i]
        currentP = P[currentPos]
        diff = currentPos + currentP[0]
        dest = diff % (N-1)

        if dest == 0:
            dest = N-1

        if currentPos <= dest:
            for j in range(currentPos+1, dest+1):
                movingP = P[j]
                _, ji = movingP
                P[j-1] = movingP
                R[ji] -= 1
        else:
            for j in range(currentPos, dest, -1):
                movingP = P[j-1]
                _, ji = movingP
                P[j] = movingP
                R[ji] += 1
        P[dest] = currentP
        R[i] = dest
        # print(d, diff, currentPos, dest)
        # print(P)
        # print(R)
        # print()

ans = 0
targets = [1000, 2000, 3000]
for target in targets:
    r = P[(R[zeroId] + target)%N][0]
    ans += r
print(ans)