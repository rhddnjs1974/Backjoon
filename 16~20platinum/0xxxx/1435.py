import sys
def ok(i, j):
    return H[i][i] * H[j][j] - H[i][j] * H[i][j] >= 0

d= []
for i in range(4):
    d.append(list(map(int,input().split())))

sq = [[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        sq[i][j] = d[i][j] * d[i][j]

H = [[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        H[i][j] = sq[i][3] + sq[j][3] - sq[i][j]

if not (ok(0, 1) and ok(0, 2) and ok(1, 2)):
    print("NO")
    exit()

det = H[0][0] * (H[1][1] * H[2][2] - H[1][2] * H[2][1])- H[0][1] * (H[1][0] * H[2][2] - H[1][2] * H[2][0])+ H[0][2] * (H[1][0] * H[2][1] - H[1][1] * H[2][0])

if det >= 0:
    print("YES")
else:
    print("NO")

