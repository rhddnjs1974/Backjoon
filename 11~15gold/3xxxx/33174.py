import sys
input = sys.stdin.readline
sys.setrecursionlimit(5*(10**5))
def makeTree(currentNode, parent):

    dp[currentNode] = A[currentNode] + dp[parent]
    for node in graph[currentNode+1]:
        makeTree(node,currentNode)


n,x = map(int,input().split())
A = list(map(int,input().split()))
P = list(map(int,input().split()))

graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]

for i in range(n):
    if P[i]!=-1:
        graph[P[i]].append(i)


dp = [1e17]*(n+1)
dp.append(0)

for i in range(n):
    if P[i]==-1:
        makeTree(i,-1)

ans = -2
for i in range(n):
    if dp[i]<=x:
        ans=i

print(ans+1)