import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

G = int(input())
P = int(input())
parent = [0] * (G + 1)

for i in range(1, G + 1):
    parent[i] = i

for i in range(1,P+1):
    g = int(input())
    t = find(g)
    if t==0:
        i=i-1
        break
    else:
        union(t,t-1)
print(i)