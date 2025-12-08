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

n,q = map(int,input().split())

arr = []

for i in range(n):
    x1,x2,y = map(int,input().split())
    arr.append((x1,x2,i))

arr.sort()

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

t = -1
x = -1
for r in range(n):
    a,b,i = arr[r]
    if a<=t:
        union(i,x)

    t = max(t,b)
    x = i


for i in range(q):
    a,b = map(int,input().split())
    if find(a-1)==find(b-1):
        print(1)
    else:
        print(0)