from my_input import sample_input
from my_input import my_input

replacement = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def solve(input, debug = False):
    lines = input.split("\n")
    if debug: print("input size =", len(lines))
    
    acc = 0
    calculatedCount = 0
    for l in lines:
        if len(l) == 0:
            continue

        found = []
        for i in range(1,10):
            if str(i) in l:
                index = l.index(str(i))
                found.append((index, str(i)))
                index = l.rindex(str(i))
                found.append((index, str(i)))
        for i in range(9):
            if replacement[i] not in l:
                continue
            index = l.index(replacement[i])
            found.append( (index, digits[i]) )
            index = l.rindex(replacement[i])
            found.append( (index, digits[i]) )
        found.sort()
        if found:
            minR = min(found)
            maxR = max(found)

            calculatedCount += 1
            s = "".join([minR[1], maxR[1]])
            if debug: print(l, s)
            acc += int(s)
    if debug: print("result:", acc)

solve(sample_input.strip(), True)
solve(my_input.strip())