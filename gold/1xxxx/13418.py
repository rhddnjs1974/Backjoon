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
V,E = map(int,input().split())

edge = []
edge2= []
parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

for i in range(E+1):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))
    edge2.append((1-c,a,b))

edge.sort()
edge2.sort()
ans = 0
ans2 = 0
for cost,x,y in edge:
    if find(x)!=find(y):
        ans+=cost
        union(x,y)


parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

for cost,x,y in edge2:
    if find(x)!=find(y):
        ans2+=cost
        union(x,y)



print((V-ans)**2-(ans2)**2)