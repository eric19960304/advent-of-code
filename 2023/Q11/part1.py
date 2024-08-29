from my_input import sample_input
from my_input import my_input

def solve(input, debug = False):
    lines = input.split("\n")
    G = lines
    # expand row
    newG = []
    for row in G:
        if row.count('#') == 0:
            newG.append([ x for x in row ])
        newG.append([ x for x in row ])
    G = newG
    # expand col
    colsToExpand = set()
    for j in range(len(G[0])):
        hasGalaxy = False
        for i in range(len(G)):
            if G[i][j] == '#':
                hasGalaxy = True
                break
        if not hasGalaxy:
            colsToExpand.add(j)

    newG = []
    for i in range(len(G)):
        newRow = []
        for j in range(len(G[0])):
            newRow.append(G[i][j])
            if j in colsToExpand:
                newRow.append('.')
        newG.append("".join(newRow))
    G = newG
    
    nodes = []
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == '#':
                nodes.append((i,j))
    M = len(nodes)

    result = 0
    for i in range(M):
        for j in range(i+1, M):
            diffX = abs(nodes[i][0] - nodes[j][0])
            diffY = abs(nodes[i][1] - nodes[j][1])
            result += diffX + diffY
    
    print(result)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())