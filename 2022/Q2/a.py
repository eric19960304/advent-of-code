from my_input import myIn

games = myIn.split("\n")
ans = 0
scoresB = {
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # X means lose, Y means draw, and Z means win
    'A': { 'X': 3,'Y': 1,'Z': 2 },
    'B': { 'X': 1,'Y': 2,'Z': 3 },
    'C': { 'X': 2,'Y': 3,'Z': 1 },
}
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
scoresA = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}
for g in games:
    [a, b] = g.split(" ")
    ans += scoresA[b]
    ans += scoresB[a][b]
print(ans)