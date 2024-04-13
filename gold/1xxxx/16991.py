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

w = [[0]*n for i in range(n)]
p = []
for i in range(n):
    a,b = map(int,input().split())
    p.append((a,b))

for i in range(n):
    for j in range(n):
        if i==j:
            continue

        x = p[i][0] - p[j][0]
        y = p[i][1] - p[j][1]

        w[i][j] = ((x**2)+(y**2) )**0.5


dp = [[-1] * (1<<n) for i in range(n)]

ans = f(0,1)
print(ans)
