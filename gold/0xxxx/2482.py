import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

dp1 = [[[0]*2 for i in range(k+1)]for j in range(n)]
dp0 = [[[0]*2 for i in range(k+1)]for j in range(n)]

dp1[0][1][1] = 1
dp0[0][0][0] = 1

for i in range(1,n):
    for j in range(k+1):
        dp1[i][j][0] = dp1[i-1][j][0] + dp1[i-1][j][1]
        dp0[i][j][0] = dp0[i - 1][j][0] + dp0[i - 1][j][1]

        if j>0:
            dp1[i][j][1] = dp1[i-1][j-1][0]
            dp0[i][j][1] = dp0[i - 1][j - 1][0]

ans = dp1[n-1][k][0]+dp0[n-1][k][0]+dp0[n-1][k][1]

ans %= 1000000003
print(ans)