import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

dist_array = [[INF]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    dist_array[a][b] = 1


for i in range(1,n+1):
    dist_array[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])


ans = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist_array[i][j] != INF:
            ans[i]+=1
            ans[j]+=1
x=0
for i in ans:
    if i==n+1:
        x+=1
print(x)