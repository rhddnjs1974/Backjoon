import sys
input = sys.stdin.readline
sys.setrecursionlimit(3*(10**5))
def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node,currentNode)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    dp[currentNode][0] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]
        dp[currentNode][0] += dp[node][0]
        dp[currentNode][0] += size[node]

n = int(input())
arr = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

for i in range(n-1):
    child[arr[i]].append(i+2)

size = [0]*(n+1)
dp = [[0]*2 for i in range(n+1)]
countSubtreeNodes(1)


for i in range(1,n+1):
    print(dp[i][0],end=" ")