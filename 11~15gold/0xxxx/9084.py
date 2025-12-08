import sys
input = sys.stdin.readline

T =int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    M = int(input())

    arr.sort()
    arr.reverse()
    dp = [0]*10001
    dp[0] = 1

    for i in arr:
        for j in range(0,10001):
            if i+j>10000:
                break
            dp[i+j] += dp[j]

    print(dp[M])