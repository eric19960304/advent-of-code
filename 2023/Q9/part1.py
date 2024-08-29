from my_input import sample_input
from my_input import my_input

def solve(input, debug = False):
    lines = input.split("\n")
    result = 0
    for line in lines:
        seqs = [[int(x) for x in line.split(" ")]]
        while any([ n!=0 for n in seqs[-1] ] ):
            nextS = []
            for i in range(len(seqs[-1])-1):
                a,b = seqs[-1][i], seqs[-1][i+1]
                nextS.append(b-a)
            seqs.append(nextS)
        for i in range(len(seqs)-2, -1, -1):
            seqs[i].append(seqs[i+1][-1] + seqs[i][-1])
        if debug: print(seqs)
        result += seqs[0][-1]
    print(result)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())