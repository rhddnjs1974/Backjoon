import math
import sys
input = sys.stdin.readline



n,l = map(int,input().split())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort()

ans = 0
e = 0

for a,b in arr:
    a = max(a,e)
    t= math.ceil((b-a)/l)

    ans += t
    e = a+l*t

print(ans)