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

n = int(input())
m = int(input())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j]==1:
            union(i+1,j+1)

plan = list(map(int,input().split()))
start= find(plan[0])
flag= 0
for i in plan:
    if find(i)!=start:
        flag=1

if flag==0:
    print("YES")
else:
    print("NO")