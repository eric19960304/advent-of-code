from my_input import my_input

def checkIfAllNodesWithZ(nodes):
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
    
    nodes = [ n for n in allNodes if n.endswith("AAA")]
    count = 0
    found = False
    while True:
        for c in commands:
            if debug: print(nodes)
            for i in range(len(nodes)):
                nodes[i] = G[nodes[i]][c]
            count += 1
            if checkIfAllNodesWithZ(nodes):
                found = True
                break
        if found:
            break
    print(count)

sample_input='''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

solve(sample_input.strip(), True)
print()
solve(my_input.strip())