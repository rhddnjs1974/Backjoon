import sys
input = sys.stdin.readline
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
#####################################################
V = int(input())
edge = []
parent = [0] * (V+1)
for i in range(V+1):
    parent[i] = i

for i in range(V):
    t = int(input())
    edge.append((t,i,V))

edge.sort()
ans = edge[0][0]
union(edge[0][1],V)

W = []

for i in range(V):
    W.append(list(map(int,input().split())))

for i in range(V):
    for j in range(i+1,V):
        edge.append((W[i][j],i,j))

edge.sort()

for cost,x,y in edge:
    if find(x)!=find(y):
        ans+=cost
        union(x,y)

print(ans)