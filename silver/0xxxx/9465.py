import sys
input = sys.stdin.readline
########################################

T = int(input())

for _ in range(T):
    n = int(input())
    arr = []
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    arr.append(A)
    arr.append(B)

    dp = [[0]*n for i in range(2)]

    dp[0][0] = A[0]
    dp[1][0] = B[0]

    for i in range(1,n):
        for j in range(2):
            if i>=2:
                dp[j][i] = max(dp[j][i-2],dp[1-j][i-2],dp[1-j][i-1]) + arr[j][i]
            else:
                dp[j][i] = dp[1-j][i-1] + arr[j][i]

    print(max(max(dp[0]),max(dp[1])))