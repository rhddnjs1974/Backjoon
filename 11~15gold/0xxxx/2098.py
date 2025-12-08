import sys
input = sys.stdin.readline

def f(a,bit):
    if bit==t:
        if w[a][0]:
            return w[a][0]
        else:
            return 1e9

    if dp[a][bit] != -1:
        return dp[a][bit]

    dp[a][bit] = 1e9

    for i in range(1,n):
        if ( not bit & (1<<i) ) and (w[a][i]!=0):
            dp[a][bit] = min(dp[a][bit], f(i, bit|(1<<i))+w[a][i])

    return dp[a][bit]


n = int(input())
t = (1<<n) -1

w = []
for i in range(n):
    w.append(list(map(int,input().split())))

dp = [[-1] * (1<<n) for i in range(n)]

ans = f(0,1)
print(ans)
