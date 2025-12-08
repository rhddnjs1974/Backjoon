import sys
sys.setrecursionlimit(10**5)
n, m = map(int,input().split())
arr = [[0]*m for i in range(n)]
dp = [[1]*m for i in range(n)]
visit = [[0]*m for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y,now):
    if arr[x][y]==0:
        dp[x][y] = 0
        return 0
    for i in range(4):
        nx = x+dx[i]*arr[x][y]
        ny = y+dy[i]*arr[x][y]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if visit[nx][ny]:
            print(-1)
            exit()
        
        visit[nx][ny] = 1
        if dp[nx][ny]==1:
            t = dfs(nx,ny,now+1)
        else:
            t = dp[nx][ny]
        visit[nx][ny] = 0

        dp[x][y] = max(dp[x][y],t+1,1)
    return dp[x][y]

for i in range(n):
    x = input().rstrip()
    for j in range(m):
        if x[j]=="H":
            arr[i][j]=0
        else:
            arr[i][j] = int(x[j])

visit[0][0] = 1

print(dfs(0,0,0))
