from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n")
data = input_data.split('\n')

ans = 0

M = len(data)
N = len(data[0])

ans = 0
for i in range(M):
    for j in range(N):
        if i==0 or i == M-1 or j==0 or j==N-1:
            continue
        score = []
        
        h = int(data[i][j])
        
        # top
        a,b = i-1,j
        d = 0
        while a >=0:
            d += 1
            if int(data[a][b]) >= h:
                break
            a-=1
        score.append(d)
        
        # left
        a,b = i,j-1
        d = 0
        while b >=0:
            
            
            d += 1
            if int(data[a][b]) >= h:
                break
            b-=1
        score.append(d)

        # down
        a,b = i+1,j
        d = 0
        while a < M:
            
            
            d += 1
            if int(data[a][b]) >= h:
                break
            a+=1
        score.append(d)

        # right
        a,b = i,j+1
        d = 0
        while b < N:
            
            d += 1
            if int(data[a][b]) >= h:
                break
            b+=1
        score.append(d)
        print(i,j,score)
        ans = max(ans, score[0]*score[1]*score[2]*score[3])
print(ans)