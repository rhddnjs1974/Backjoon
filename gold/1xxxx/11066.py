import sys
input = sys.stdin.readline
########################################

T = int(input())

for t in range(T):
    K = int(input())
    arr = [0]+list(map(int,input().split()))
    sarr = []
    s=0
    for i in arr:
        s +=i
        sarr.append(s)

    dp = [[1e9]*(K+1) for i in range(K+1)]
    for i in range(1,K+1):
        dp[i][i] = 0

    for i in range(2,K+1): # 길이
        for j in range(1,K+1):
            if i+j>K+1:
                break
            for m in range(j,j+i-1):
                dp[j][j+i-1]= min(dp[j][j+i-1],dp[j][m]+dp[m+1][j+i-1]+sarr[j+i-1]-sarr[j-1])

    print(dp[1][K])