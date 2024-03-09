import sys
input = sys.stdin.readline
########################################

T = int(input())

for i in range(T):
    K = int(input())
    arr = list(map(int,input().split()))
    dp = [1e9]*K
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    for i in range(2,K):
        dp[i] = min(dp[i-2]*2+(arr[i-1]+arr[i])*2,dp[i-1]*2+arr[i])
    print(dp)