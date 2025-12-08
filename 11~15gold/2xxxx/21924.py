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
parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

total  =0
for i in range(E):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))
    total+=c

edge.sort()
ans = 0
num = 0

for cost,x,y in edge:
    if find(x)!=find(y):
        ans+=cost
        union(x,y)
        num+=1
if num==V-1:
    print(total-ans)
else:
    print(-1)