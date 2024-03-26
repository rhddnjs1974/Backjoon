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

v, e = map(int, input().split())
parent = [0] * (v + 1)

know = list(map(int,input().split()))


for i in range(1, v + 1):
    parent[i] = i

party = [0] * e

for i in range(e):
    a,*arr = map(int, input().split())
    one = arr[0]
    party[i]=one
    for i in arr[1:]:
        union(one,i)

for i in range(1,len(know)):
    know[i] = find(know[i])

ans = 0
for i in party:
    if find(i) not in know[1:]:
        ans+=1


print(ans)