import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dist_array = [[INF]*(n) for i in range(n)]

array = []
for i in range(n):
    array.append(input())

for i in range(n):
    for j in range(n):
        if array[i][j]=="Y":
            dist_array[i][j]=1
        else:
            dist_array[i][j]=INF

for i in range(n):
    dist_array[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])


ans = [[0]*(n) for i in range(n)]

for i in range(n):
    for j in range(n):
        if 0<dist_array[i][j] <= 2:
            ans[i][j]=1
            ans[j][i]=1

ma = 0
for i in ans:
    ma = max(ma,sum(i))

print(ma)