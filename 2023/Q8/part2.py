from my_input import my_input
from math import gcd

def checkIfNodesEndWithZ(nodes):
    for node in nodes:
        if not node.endswith('Z'):
            return False
    return True

def solve(input, debug = False):
    lines = input.split("\n\n")
    commands = lines[0]
    positions = lines[1].split("\n")
    G = {}
    allNodes = []
    for p in positions:
        source = p.split(" = ")[0]
        dests = p.split(" = ")[1].split(", ")
        leftD = dests[0][1:]
        rightD = dests[1][:-1]
        G[source] = {'L': leftD, 'R': rightD}
        allNodes.append(source)
    
    nodes = [ n for n in allNodes if n.endswith("A")]
    counts = []
    for node in nodes:
        count = 0
        found = False
        while True:
            for c in commands:
                node = G[node][c]
                count += 1
                if checkIfNodesEndWithZ([node]):
                    found = True
                    break
            if found:
                break
        counts.append(count)
    if debug: print(counts)
    lcm = 1
    for i in counts:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)

sample_input='''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''

solve(sample_input.strip(), True)
print()
solve(my_input.strip())