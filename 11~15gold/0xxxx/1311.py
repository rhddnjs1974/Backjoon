import sys
input = sys.stdin.readline
def f(a,bit):
    if a==n:
        return 0
    if dp[bit] != -1:
        return dp[bit]
    dp[bit] = 1e9
    for i in range(n):
        if not bit & (1<<i):
            dp[bit] = min(dp[bit], f(a+1, bit|(1<<i))+d[a][i])
    return dp[bit]


n = int(input())
d = []
for i in range(n):
    d.append(list(map(int,input().split())))

dp = [-1] * (1<<20)

ans = f(0,0)
print(ans)