import sys
import heapq
input = sys.stdin.readline
n = int(input())

arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((min(a,b),max(a,b)))

arr.sort(key=lambda x:(x[1],x[0]))

d = int(input())

count = 0
ans = 0
heap = []
for a,b in arr:
    if a>=b-d:
        heapq.heappush(heap,a)
        count +=1

    t = -1e10
    k = 0
    while(heap):
        t = heapq.heappop(heap)
        k = 0
        if t<b-d:
            count-=1
            k = 1
        else:
            break
    if t!=-1e10 and k==0:
        heapq.heappush(heap,t)

    ans = max(ans,count)

print(ans)