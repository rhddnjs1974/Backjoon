N, K =map(int,input().split())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
    
ans = [[0]*(N*K) for i in range(N*K)]

for i in range(N*K):
    for j in range(N*K):
        x = i//K
        y = j//K
        ans[i][j] = arr[x][y]

for i in ans:
    print(*i)