from my_input import sample_input
from my_input import my_input

from collections import deque

def hash(c, val):
    val += ord(c)
    val *= 17
    val = val % 256
    return val

def indexByLabel(box, label):
    pos = -1
    for i, (l, _) in enumerate(box):
        if l == label:
            pos = i
            break
    return pos

def decode(label):
    h = 0
    for c in label:
        h = hash(c, h)
    return h

def findFocals(boxes, command):
    if '-' in command:
        label = command.split("-")[0]
        boxNum = decode(label)

        delPos = indexByLabel(boxes[boxNum], label)
        if delPos != -1:
            del boxes[boxNum][delPos]
    else:
        label = command.split("=")[0]
        boxNum = decode(label)

        number = int(command.split("=")[1])
        index = indexByLabel(boxes[boxNum], label)
        if index == -1:
            boxes[boxNum].append((label, number))
        else:
            boxes[boxNum][index] = (label, number)
    

def solve(input, debug = False):
    commands = input.split(",")
    
    boxes = [ deque([]) for _ in range(256) ]
    for command in commands:
        findFocals(boxes, command)
    if debug:
        for i in range(256):
            if boxes[i]:
                print(f"{i}: {boxes[i]}")
    result = 0
    for i in range(256):
        for j in range(len(boxes[i])):
            result += (i+1) * (j+1) * boxes[i][j][1]
    print(result)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())