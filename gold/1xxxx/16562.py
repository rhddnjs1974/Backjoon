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
    if want[a] < want[b]:
        parent[b] = a
    else:
        parent[a] = b

v, e, k = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

want = [0]+list(map(int,input().split()))


for i in range(e):
    a,b = map(int, input().split())
    union(a,b)

ans = 0
for i in range(1,v+1):
    x = find(i)
    if x!=0:
        ans+=want[x]
        parent[x] = 0

if ans<=k:
    print(ans)
else:
    print("Oh no")
