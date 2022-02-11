ways = []
for _ in range(21):
    ways.append([0]*21)
for i in range(21):
    ways[i][0] = 1
    ways[0][i] = 1

for i in range(1,21):
    for j in range(1,21):
        ways[i][j] = ways[i-1][j] + ways[i][j-1]

print(ways[20][20])
