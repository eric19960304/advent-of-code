from my_input import sample_input
from my_input import my_input

hitHistory = set()

def countXMAS(G, i, j):
    M = len(G)
    N = len(G[0])

    hit = 0
    stack = [(i, j, G[i][j], c) for c in range(8)]
    while stack:
        u = stack.pop()
        ui, uj, accStr, c = u
        if accStr == "XMAS":
            hit += 1
            hitHistory.add((ui, uj))
            continue
        
        possibleMoves = [(ui+1, uj), (ui-1, uj), (ui, uj+1), (ui, uj-1), \
                  (ui+1, uj+1), (ui+1, uj-1), (ui-1, uj-1), (ui-1, uj+1)]

        vi, vj = possibleMoves[c]

        if not (0 <= vi < M and 0 <= vj < N):
            continue

        newAccStr = accStr + G[vi][vj]
        if not "XMAS".startswith(newAccStr):
            continue

        stack.append( (vi, vj, newAccStr, c) )
    return hit

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
            ans += countXMAS(G, i, j)
    if debug:
        for i in range(M):
            row = []
            for j in range(N):
                if (i,j) in hitHistory:
                    row.append(G[i][j])
                else:
                    row.append('.')
            print("".join(row))
        print()
    print(ans)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())