from my_input import sample_input
from my_input import my_input

def isValid(M, N, i, j):
    return 0 <= i < M and 0 <= j < N

def solve(input_s, debug = False):
    G = []
    ans = 0

    lines = input_s.split("\n")
    for line in lines:
        G.append(list(line))
    
    M = len(G)
    N = len(G[0])
    for i in range(M):
        for j in range(N):
            if G[i][j] != 'A':
                continue
            checklist = [(i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]
            if not all([ isValid(M, N, a, b) for a,b in checklist ]):
                continue
            grp1 = [ G[i+1][j+1],  G[i-1][j-1]]
            grp2 = [ G[i+1][j-1],  G[i-1][j+1]]
            if "".join(sorted(grp1)) == "MS" and "".join(sorted(grp2)) == "MS":
                ans += 1
    print(ans)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())