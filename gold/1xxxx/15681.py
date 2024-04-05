import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
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

n,r,q = map(int,input().split())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

size = [0]*(n+1)
for i in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(r,-1)
countSubtreeNodes(r)

for i in range(q):
    a = int(input())
    print(size[a])