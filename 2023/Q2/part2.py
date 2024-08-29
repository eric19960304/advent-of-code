from my_input import sample_input, my_input

colors = ['blue', 'red', 'green']
DEBUG = False

def parseGameRecord(records):
    parsedRecords = {}
    srecords = records.strip().split(", ")
    for srecord in srecords:
        for color in colors:
            if color in srecord:
                parsedRecords[color] = int(srecord.split(" ")[0])
    return parsedRecords

def parseInput(line):
    sline = line.split(":")
    gameId = int(sline[0].split(" ")[1])
    gameRecords = sline[1].split(";")
    parsedGameRecords = []
    for record in gameRecords:
        parsedGameRecords.append(parseGameRecord(record))
    return (gameId, parsedGameRecords)

def findPower(gameRecords):
    colorMin = { 'red': 0, 'green': 0, 'blue': 0 }
    for gameRecord in gameRecords:
        for color in colors:
            if color in gameRecord:
                colorMin[color] = max(colorMin[color], gameRecord[color])
    power = 1
    for k,v in colorMin.items():
        power *= v
    return power

def solve(input):
    lines = input.split("\n")
    if DEBUG: print("input size =", len(lines))
    res = 0

    for line in lines:
        (gameId, gameRecords) = parseInput(line)
        if DEBUG: print("gameId", gameId, "gameRecords", gameRecords)
        res += findPower(gameRecords)
    
    print(res)

solve(sample_input.strip())
print()
solve(my_input.strip())