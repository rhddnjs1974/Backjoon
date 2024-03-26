import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    global i,flag
    a = find(a)
    b = find(b)
    if a==b:
        print(i+1)
        flag = 1
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i
flag=0
for i in range(e):
    a,b = map(int, input().split())
    union(a,b)
    if flag==1:
        break

if flag==0:
    print(0)