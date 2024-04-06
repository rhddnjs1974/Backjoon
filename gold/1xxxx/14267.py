import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def countSubtreeNodes(currentNode):
    dp[currentNode] += good[currentNode]
    for node in child[currentNode]:
        dp[node] += dp[currentNode]
        countSubtreeNodes(node)


n,m = map(int,input().split())
child = [[] for i in range(n+1)]

arr= list(map(int,input().split()))
for i in range(n):
    p = arr[i]
    if p!=-1:
        child[p].append(i+1)

dp = [0]*(n+1)

good = [0]*(n+1)

for i in range(m):
    u,v = map(int,input().split())
    good[u] += v



countSubtreeNodes(1)

print(*dp[1:])