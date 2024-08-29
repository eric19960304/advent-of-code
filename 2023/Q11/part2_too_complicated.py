from my_input import sample_input
from my_input import my_input

import heapq

million = 100

def solve(input, debug = False):
    lines = input.split("\n")
    G = lines
    # expand row
    newG = []
    for row in G:
        if row.count('#') == 0:
            newG.append([ '-' for _ in range(len(G[0])) ])
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
                if G[i][j] == '.':
                    newRow.append('|')
                else:
                    newRow.append('+')
        newG.append("".join(newRow))
    G = newG
    
    nodes = []
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == '#':
                nodes.append((i,j))
    M = len(nodes)

    allPairDistances = {}
    for node in nodes:
        allPairDistances[node] = {}
    
    def getCost(d, cell):
        if cell == '+':
            return million

        if cell == '|' and d in ['E', 'W']:
            return million
        
        if cell == '-' and d in ['S', 'N']:
            return million

        return 1
        

    def bfs(G, targetNodes, source):
        M = len(G)
        N = len(G[0])
        Q = [ (0, source) ] # (node, distance)
        heapq.heapify(Q)
        distance = {}
        V = set()
        while Q:
            d, u = heapq.heappop(Q)
            V.add(u)

            if u in targetNodes and u != source:
                distance[u] = d
                if len(distance.keys()) == len(targetNodes) - 1:
                    break

            i,j = u
            adjs = [
                (i+1, j, 'S'), 
                (i-1, j, 'N'), 
                (i, j+1, 'E'), 
                (i, j-1, 'W')
            ]
            for a, b, direction in adjs:
                isInBound = 0 <= a < M and 0 <= b < N
                if isInBound and (a,b) not in V:
                    cost = getCost(direction, G[i][j])
                    nextItem = (d + cost, (a,b))
                    heapq.heappush(Q, nextItem)
        return distance
    
    targetNodes = set(nodes)
    for i in range(M):
        print('calculating {}/{}'.format(i, M))
        node = nodes[i]
        allPairDistances[node] = bfs(G, targetNodes, node)
        targetNodes.remove(node)
    
    result = 0
    for i in range(M):
        for j in range(i+1, M):
            result += allPairDistances[nodes[i]][nodes[j]]
    print(result - M*M - 1)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())