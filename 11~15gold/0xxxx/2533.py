import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node,currentNode)

def countSubtreeNodes(currentNode):
    dp[currentNode][0] = 0
    dp[currentNode][1] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        dp[currentNode][0] += dp[node][1]
        dp[currentNode][1] += min(dp[node][0],dp[node][1])

n = int(input())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

dp = [[0]*2 for i in range(n+1)]
for i in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(1,-1)
countSubtreeNodes(1)


print(min(dp[1]))