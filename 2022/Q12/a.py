from collections import deque
import heapq

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')



M = len(data)
N = len(data[0])

ans = []
for i in range(M):
    for j in range(N):
        if data[i][j] != 'a':
            continue
    
        Q = [(0,i, j)]
        V = set()
        
        while Q:
            u = heapq.heappop(Q)
            count,a,b = u

            if data[a][b] == 'E':
                ans.append(count)
                break
            
            V.add( (a,b) )

            print(u, data[a][b])

            elevation = ord(data[a][b]) if data[a][b] != 'S' else ord('a')-1

            adjs = [(a+1,b),(a,b+1),(a-1,b),(a,b-1)]
            adjs = list(filter(lambda z: z[0] >= 0 and z[0] < M and z[1] >=0 and z[1] < N, adjs))

            for v in adjs:
                x,y = v
                if (x,y) in V:
                    continue
                
                newElevation = ord(data[x][y]) if data[x][y] != 'E' else ord('z')+1
                if elevation + 1 == newElevation or elevation >= newElevation:
                    newVisit = (count+1, x, y)
                    heapq.heappush(Q, newVisit)
                    V.add((x,y))
print(min(ans))