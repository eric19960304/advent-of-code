from my_input import myIn

xs = myIn.split("\n\n")
print(xs[:3])
numsGroup = [ [ int(s) for s in x.split("\n")] for x in xs ]
print(numsGroup[0])

sums = [ sum(g) for g in numsGroup ]
sums.sort()

print(sums[-1])
print(sums[-3:])
print(sum(sums[-3:]))