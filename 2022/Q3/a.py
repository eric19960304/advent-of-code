from my_input import myIn
from sample import sameple

games = myIn.split("\n")

ans = 0

back = []

groups = []
i=0
while i < len(games):
    groups.append([games[i], games[i+1], games[i+2]])
    i+=3

for g in groups:
    a = set(g[0])
    b = set(g[1])
    c = set(g[2])
    # print(g[:n//2])
    # print(g[n//2:])
    c = list(a.intersection(b).intersection(c))
    c = c[0]
    print(c)
    if c >= 'a' and c <='z':
        back.append(ord(c) - ord('a') + 1)
    else:
        back.append(ord(c) - ord('A') + 27)
print(sum(back))