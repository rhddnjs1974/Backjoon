import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
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

V = int(input())

edge = []
parent = [0] * (V)
for i in range(V):
    parent[i] = i

co = []
for i in range(V):
    a,b,c = map(int,input().split())
    co.append((a,b,c))
    for j in range(i):
        d = min(abs(a-co[j][0]),abs(b-co[j][1]),abs(c-co[j][2]))
        edge.append((d,i,j))

edge.sort()
ans = 0


for cost,x,y in edge:
    if find(x)!=find(y):
        ans+=cost
        union(x,y)

print(ans)