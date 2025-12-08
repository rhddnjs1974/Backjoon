import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(i):
    if parent[i] == i:
        return i
    
    parent[i] = find(parent[i])
    return parent[i]

def union(i,j):
    if i<j:
        parent[find(i)] = find(j)
    else:
        parent[find(j)] = find(i)


n,m = map(int,input().split())
parent = []
for i in range(n+1):
    parent.append(i)
    
for i in range(m):
    x,a,b = map(int,input().split())
    if x==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print("yes")
        else:
            print("no")