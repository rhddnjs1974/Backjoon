import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    global ans
    a = find(a)
    b = find(b)
    if a==b:
        try:
            ans.remove(a)
        except:
            return
        return
    if a < b:
        parent[b] = a
        if b in ans:
            ans.remove(b)
        else:
            if a in ans:
                ans.remove(a)

    else:
        parent[a] = b
        if a in ans:
            ans.remove(a)
        else:
            if b in ans:
                ans.remove(b)

t=0
while(True):
    t+=1
    n, m = map(int, input().split())
    if n==m==0:
        break
    parent = [0] * (n + 1)
    ans = set()

    for i in range(1, n + 1):
        ans.add(i)
        parent[i] = i


    for i in range(m):
        a,b = map(int, input().split())
        union(a,b)

    x = len(ans)

    print("Case %d: "%(t),end="")
    if x==0:
        print("No trees.")
    elif x==1:
        print("There is one tree.")
    else:
        print("A forest of %d trees."%(x))
