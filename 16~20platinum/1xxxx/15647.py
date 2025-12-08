import sys
input = sys.stdin.readline
sys.setrecursionlimit(4*(10**5))

def countSubtreeNodes(currentNode, parent):
    global basicdist
    size[currentNode] = 1
    for node,dist in graph[currentNode]:
        if node != parent:
            countSubtreeNodes(node,currentNode)
            basicdist+= dist*size[node]
            size[currentNode] += size[node]

def dfs(currentNode):
    global n
    for node,dist in graph[currentNode]:
        if dpdist[node]==0:
            dpdist[node] = dpdist[currentNode]-dist*(2*size[node]-n)
            dfs(node)

n = int(input())
graph = [[] for i in range(n+1)]

size = [0]*(n+1)
for i in range(n-1):
    u,v,d = map(int,input().split())
    graph[u].append((v,d))
    graph[v].append((u,d))

basicdist = 0
countSubtreeNodes(1,-1) #size 제작

dpdist = [0]*(n+1)
dpdist[1] = basicdist
dfs(1)

for i in range(1,n+1):
    print(dpdist[i])