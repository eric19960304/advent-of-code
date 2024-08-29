from my_input import myIn
from sample import sameple

# pairs = sameple.split("\n")
pairs = myIn.split("\n")

count = 0
for p in pairs:
    [a,b] = p.split(",")
    [aS,aE] = [int(x) for x in a.split("-")]
    [bS,bE] = [int(x) for x in b.split("-")]
    if aS <= bS <= aE or aS <= bE <= aE or \
        bS <= aS <= bE:
        count += 1
print(count)