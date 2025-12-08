import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def makeTree(currentNode, parent):
    for node,w in graph[currentNode]:
        if node != parent:
            child[currentNode].append((node,w))
            makeTree(node,currentNode)

def countSubtreeNodes(currentNode):
    dp[currentNode] = 0
    for node,ww in child[currentNode]:
        countSubtreeNodes(node)
        dp[currentNode] += ww
        dp[currentNode] += (ww+1)*dp[node]

n = int(input())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

dp = [0] * (n+1)
for i in range(n-1):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

makeTree(1,-1)
countSubtreeNodes(1)

print(dp)