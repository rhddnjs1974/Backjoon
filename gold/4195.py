import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    global network
    a = find(a)
    b = find(b)
    if a==b:
        return
    if a < b:
        parent[b] = a
        network[a]+=network[b]
    else:
        parent[a] = b
        network[b]+=network[a]
T = int(input())

for i in range(T):
    v = int(input())
    parent = [0] * (1+v*2)

    for i in range(1+v*2):
        parent[i] = i

    member = 0
    dic = {}

    network = [1]*(1+v*2)

    for i in range(v):
        a,b = input().split()
        if a not in dic:
            dic[a] = member
            member += 1
        if b not in dic:
            dic[b] = member
            member += 1

        union(dic[a],dic[b])

        print(network[find(dic[a])])