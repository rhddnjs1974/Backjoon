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
parent = [0] * (V)
for i in range(V):
    parent[i] = i

point = []
for i in range(V):
    a,b = map(float,input().split())
    point.append((a,b))


for i in range(V):
    for j in range(i+1,V):
        cost = ((point[i][0]-point[j][0])**2+(point[i][1]-point[j][1])**2)**0.5
        edge.append((cost,i,j))

edge.sort()
ans = 0

for cost,x,y in edge:
    if find(x)!=find(y):
        ans+=cost
        union(x,y)

print(ans)