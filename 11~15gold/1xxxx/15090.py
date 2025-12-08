import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node,currentNode)

def countSubtreeNodes(currentNode):
    global n
    size[currentNode] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]
        dp[currentNode].append(size[node])
    t = sum(dp[currentNode])
    dp[currentNode].append(n-t)
    
n = int(input())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

size = [0]*(n+1)
dp = [[] for i in range(n+1)]

for i in range(n):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(0,-1)
countSubtreeNodes(0)

ma = 0
id = 0
for i in range(n+1):
    a=0
    for x in itertools.combinations(dp[i],2):
        a+= x[0]*x[1]
    if ma<a:
        ma = a
        id = i


dp[id].sort()
dp[id][-1] = dp[id][-1]+dp[id][-2]
dp[id][-2] = 0

a=0
for x in itertools.combinations(dp[id],2):
    a+= x[0]*x[1]
print(ma,a)