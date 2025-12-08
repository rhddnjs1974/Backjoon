import sys
input = sys.stdin.readline
import math
sys.setrecursionlimit(10**5)
def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node,currentNode)

def countSubtreeNodes(currentNode):
    for i in range(x):
        dp[currentNode][i]= i+1

    for node in child[currentNode]:
        countSubtreeNodes(node)
        for i in range(x):
            mi = 1e9
            for j in range(x):
                if i==j:
                    continue
                mi = min(mi,dp[node][j])
            dp[currentNode][i] += mi


n = int(input())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

x = math.ceil(math.log2(n))


dp = [[0]*x for i in range(n+1)]
for i in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(1,-1)
countSubtreeNodes(1)

print(min(dp[1]))
