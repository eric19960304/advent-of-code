from my_input import sample_input, my_input

colorLimit = { 'red': 12, 'green': 13, 'blue': 14 }
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

def checkColors(gameRecord):
    for color in colors:
        if color in gameRecord and colorLimit[color] < gameRecord[color]:
            return False
    return True

def solve(input):
    lines = input.split("\n")
    if DEBUG: print("input size =", len(lines))
    res = 0

    for line in lines:
        (gameId, gameRecords) = parseInput(line)
        if DEBUG: print("gameId", gameId, "gameRecords", gameRecords)
        if all([ checkColors(gameRecord) for gameRecord in gameRecords]):
            res += gameId
    
    print(res)

solve(sample_input.strip())
print()
solve(my_input.strip())