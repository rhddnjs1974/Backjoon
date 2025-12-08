n = int(input())
graph = [[0]*(n+1) for i in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

ans = []
k=0
if 2*n-2>=n*(n-1)/2:
    r=1
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if graph[i][j]==0:
                ans.append((i,j))
                k+=1
else:
    r=2
    for i in range(2,n+1):
        if graph[1][i]==0:
            ans.append((1,i))
            k+=1

print(k)
print(r)
for a,b in ans:
    print(a,b)