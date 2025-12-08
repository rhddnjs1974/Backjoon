import sys
input = sys.stdin.readline
sys.setrecursionlimit(6*(10**5))
def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node,currentNode)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]

n = int(input())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

edge = []

size = [0]*(n+1)
for i in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    edge.append((u,v))
    
makeTree(1,-1)
countSubtreeNodes(1)

ans = 0
for x,y in edge:
    now = min(size[x],size[y])
    ans += (now*(now-1))//2
    ans += (now)*(n-now)
print(ans)