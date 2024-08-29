from my_input import sample_input
from my_input import my_input

expansionSize = 1000000

def solve(input, debug = False):
    lines = input.split("\n")
    G = lines
    # find expanding row
    rowsToExpand = set()
    for i in range(len(G)):
        row = G[i]
        if row.count('#') == 0:
            rowsToExpand.add(i)
    
    # find expanding col
    colsToExpand = set()
    for j in range(len(G[0])):
        hasGalaxy = False
        for i in range(len(G)):
            if G[i][j] == '#':
                hasGalaxy = True
                break
        if not hasGalaxy:
            colsToExpand.add(j)
    
    nodes = []
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == '#':
                nodes.append((i,j))
    M = len(nodes)

    result = 0
    for i in range(M):
        for j in range(i+1, M):
            distance = 0
            diffY = abs(nodes[i][0] - nodes[j][0])
            diffX = abs(nodes[i][1] - nodes[j][1])
            distance += diffX + diffY

            ys = [nodes[i][0], nodes[j][0]]
            xs = [nodes[i][1], nodes[j][1]]
            ys.sort()
            xs.sort()
            x1,x2 = xs
            y1,y2 = ys
            for c in colsToExpand:
                if x1 < c < x2:
                    distance += expansionSize - 1
            for r in rowsToExpand:
                if y1 < r < y2:
                    distance += expansionSize - 1
            if debug: print(nodes[i], nodes[j], distance)
            result += distance
    print(result)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())