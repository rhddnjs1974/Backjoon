n,m = map(int,input().split())

inf = 1e9

arr = []
dp = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    dp.append([[inf,inf,inf] for i in range(m)]) #좌하, 하, 우하

for i in range(m):
    for j in range(3):
        dp[0][i][j] = arr[0][i]


for i in range(1,n):
    for j in range(m):
        for k in range(3):

            if j==0:
                if k!=1:
                    dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][1]+arr[i][j])
                if k!=0:
                    dp[i][j][k] = min(dp[i][j][k],dp[i-1][j+1][0]+arr[i][j])  
            elif j==m-1:
                if k!=1:
                    dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][1]+arr[i][j])
                if k!=2:
                    dp[i][j][k] = min(dp[i][j][k],dp[i-1][j-1][2]+arr[i][j])
            else:
                if k!=1:
                    dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][1]+arr[i][j])
                if k!=2:
                    dp[i][j][k] = min(dp[i][j][k],dp[i-1][j-1][2]+arr[i][j])
                if k!=0:
                    dp[i][j][k] = min(dp[i][j][k],dp[i-1][j+1][0]+arr[i][j]) 


ans = 1e9
for i in range(m):
    for j in range(3):
        ans = min(ans,dp[n-1][i][j])

print(ans)