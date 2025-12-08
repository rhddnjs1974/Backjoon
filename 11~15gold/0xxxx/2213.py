import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node,currentNode)

def countSubtreeNodes(currentNode):
    dp[currentNode][1] = arr[currentNode]

    for node in child[currentNode]:
        countSubtreeNodes(node)
        dp[currentNode][0] += max(dp[node][1],dp[node][0])
        dp[currentNode][1] += dp[node][0]

n = int(input())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

arr = [0]+list(map(int,input().split()))

dp = [[0]*2 for i in range(n+1)] #1 : 포함 0 :포함x
for i in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(1,-1)
countSubtreeNodes(1)

print(max(dp[1]))
ans = []
if dp[1][0]<dp[1][1]:
    ans.append(1)

q = deque()
q.append(1)

while(q):
    x = q.pop()
    for i in child[x]:
        q.append(i)
        if x not in ans:
            if dp[i][0]<dp[i][1]:
                ans.append(i)

ans.sort()
print(*ans)