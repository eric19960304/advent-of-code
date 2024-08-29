from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n\n")
data = input_data.split("\n\n")

mapping = data[0]
data = data[1]

mapping = mapping.split("\n")
mapping = mapping[:-1]
indexes = [1, 5, 9, 13, 17, 21, 25, 29, 33]
S = [ [] for i in range(len(indexes)) ]
mapping.reverse()
for m in mapping:
    for i in range(len(indexes)):
        if m[indexes[i]] != ' ':
            S[i].append(m[indexes[i]])

# print(S)

for d in data.split("\n"):
    digits = d.split(" ")
    digits = list(filter(lambda x: x[0] >= '0' and x[0] <= '9' , digits))
    digits = [ int(x) for x in digits]
    [n, src, dst] = [int(x) for x in digits]
    # print(n, src, dst)
    
    # print(S, digits)
    realSrc = src-1
    realDst = dst-1
    gs = []
    for i in range(n):
        gs.append(S[realSrc].pop())
    gs.reverse()
    S[realDst].extend(gs)
    

# print(S)
ans = ''
for i in range(len(S)):
    if S[i][-1] != '':
        ans += S[i][-1]
print(ans)