import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################
sys.setrecursionlimit(1000000)
def dfs(start):

    visit[start]=1
    if len(graph[start])==1:
        dp[start] = graph[start][0][1]
        dp2[start] = 1e9

    for node,value in graph[start]:
        if visit[node]==0:
            dp[node] = value
            dfs(node)
            dp2[start] += dp[node]


    dp[start] = min(dp[start],dp2[start])


N = int(input())
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a,b,v = map(int,input().split())
    graph[a].append((b,v))
    graph[b].append((a,v))

dp = [1e9] * (N+1)
dp2 = [0] * (N+1)
visit = [0]*(N+1)

dfs(1)
print(dp[1])


