import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dist_array = [[INF]*(n+1) for i in range(n+1)]

while(True):
    a,b = map(int,input().split())
    if a==b==-1:
        break
    dist_array[a][b] = 1
    dist_array[b][a] = 1

for i in range(1,n+1):
    dist_array[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])

mi = 51
ans = []
for i in range(1,n+1):
    x = max(dist_array[i][1:])
    if x<mi:
        ans = [i]
        mi = x
    elif x==mi:
        ans.append(i)

print(mi,len(ans))
print(*ans)