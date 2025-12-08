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

arr = [0]+list(input().split())

edge = []
parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    a,b,c = map(int,input().split())
    if arr[a]!=arr[b]:
        edge.append((c,a,b))

edge.sort()
ans = 0
num = 0

for cost,x,y in edge:
    if find(x)!=find(y):
        num+=1
        ans+=cost
        union(x,y)

if num==V-1:
    print(ans)
else:
    print(-1)