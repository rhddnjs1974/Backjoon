import sys
input = sys.stdin.readline
########################################
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(a,b):
    if dp[a][b]!=-1:
        return dp[a][b]

    ret = 0
    for i in range(4):
        na = a+dx[i]
        nb = b+dy[i]
        if na<0 or na>=N or nb<0 or nb>=M:
            continue
        if arr[na][nb]>=arr[a][b]:
            continue

        ret += dfs(na,nb)

    dp[a][b] = ret
    return ret

N,M = map(int,input().split())
arr= []
for i in range(N):
    arr.append(list(map(int,input().split())))

dp = [[-1]*M for i in range(N)]
dp[N-1][M-1] = 1

dfs(0,0)
print(dp[0][0])