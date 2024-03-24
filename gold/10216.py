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

T = int(input())
for i in range(T):
    v = int(input())
    parent = [0] * (v)

    for i in range(v):
        parent[i] = i

    arr = []

    for i in range(v):
        x,y,r = map(int,input().split())
        for j in range(len(arr)):
            xx,yy,rr = arr[j]
            dist2 = (x-xx)**2 + (y-yy)**2
            if dist2<=(r+rr)**2:
                union(i,j)

        arr.append((x,y,r))

    ans = set()
    for i in range(v):
        ans.add(find(i))
    print(len(ans))