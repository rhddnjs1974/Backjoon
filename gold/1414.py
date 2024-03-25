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

arr = []
for i in range(V):
    arr.append(input())

total =0
for i in range(V):
    for j in range(V):
        t = ord(arr[i][j])
        if t==48:
            continue
        if 65<=t<=90:
            t-=38
        else:
            t-=96

        edge.append((t,i,j))
        total += t

edge.sort()
ans = 0
num = 0

for cost,x,y in edge:
    if find(x)!=find(y):
        ans+=cost
        union(x,y)
        num+=1

if num == V-1:
    print(total-ans)
else:
    print(-1)