import sys

input = sys.stdin.readline

n,t,m = map(int,input().split())
s,e = map(int,input().split())

graph = [[] for _ in range(n)]
dp = [1e9]*n
dp[s] = 0

for i in range(t):
    dp2 = [1e9]*n
    se = set()
    for _ in range(m):
        a,b,w = map(int,input().split())
        se.add(a)
        se.add(b)
        dp2[a] = min(dp2[a],dp[b]+w)
        dp2[b] = min(dp2[b],dp[a]+w)
    
    for x in se:
        dp[x] = min(dp[x],dp2[x])

if dp[e]==1e9:
    print(-1)
else:
    print(dp[e])