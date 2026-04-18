# 라이브러리: 펜윅트리.py
import sys
input = sys.stdin.readline

def update(i,dif):
    while(i<=n):
        fenwick[i] += dif
        i += (i & -i)

def subsum(i):
    ans = 0
    while(i>0):
        ans += fenwick[i]
        i -= (i & -i)
    return ans

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos = {}
for i in range(n):
    pos[a[i]] = i+1

fenwick = [0] * (n+1)
ans = 0
for j in range(n):
    p = pos[b[j]]
    ans += j-subsum(p)
    update(p, 1)

print(ans)
