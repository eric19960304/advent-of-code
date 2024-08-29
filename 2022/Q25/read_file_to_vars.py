
from parse import parse

def readfile(file):
    with open(file) as f:
        lines = f.readlines()

    data = []
    for l in lines:
        vars = parse(
            "Blueprint {i}: Each ore robot costs {oror} ore. Each clay robot costs {clor} ore. Each obsidian robot costs {obor} ore and {obcl} clay. Each geode robot costs {geor} ore and {geob} obsidian.",
            l.strip(),
        ).named
        data.append({k: int(v) for k, v in vars.items()})

    return data

FILE_NAME = 'puzzle_input.txt'
FILE_NAME = 'puzzle_sample.txt'

data_vars = readfile(FILE_NAME)
print(FILE_NAME, 'length:', len(data_vars))
print()