import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((min(a,b),max(a,b)))

arr.sort(key=lambda x:(x[0]))


count = 0
ans = 0
heap = []
for a,b in arr:
    heapq.heappush(heap,b)
    count +=1

    t = -1e10
    while(heap):
        t = heapq.heappop(heap)

        if t<=a:
            count-=1
        else:
            break
    if t!=-1e10:
        heapq.heappush(heap,t)

    ans = max(ans,count)

print(ans)