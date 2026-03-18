import heapq
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = [1e9 for i in range(n)]
e = []
for i in range(m):
    a,b,c = map(int, input().split())
    e.append((a,b,-c))

d[0] = 0
isdone = False
arr = [1e9 for i in range(n)]
for i in range(2*n):
    for j in e:
        if d[j[0]-1] < 1e8 and d[j[1]-1] > d[j[0]-1] + j[2]:
            d[j[1]-1] = d[j[0]-1] + j[2]
            arr[j[1]-1] = j[0]
            if i >= n-1 and j[1] == n:
                print(-1)
                isdone = True
                break
    if isdone:
        break

if d[-1] > 1e8:
    print(-1)
    isdone = True

ans = [n]
if not isdone:
    t = n
    while(t != 1):
        ans.append(arr[t-1])
        t= arr[t-1]
    ans.reverse()
    print(*ans)