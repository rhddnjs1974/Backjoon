t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [[0 for i in range(n+1)] for i in range(k+1)]
    
    for i in range(n+1):
        dp[0][i] = i
    
    for i in range(1,k+1):
        for j in range(n+1):
            for r in range(j+1):
                dp[i][j] += dp[i-1][r]

    print(dp[k][n])