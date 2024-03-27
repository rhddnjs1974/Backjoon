import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
############################################

n,k = map(int,input().split())

arr = []
for i in range(n):
    a,b = map(int,input().split())
    heapq.heappush(arr,(a,b))
arr.sort()

C = []
for i in range(k):
    C.append(int(input()))

C.sort()
ans = 0
heap = []

for i in C:
    while(arr):
        a,b = heapq.heappop(arr)
        if a<=i:
            heapq.heappush(heap,(-b))
        else:
            heapq.heappush(arr,(a,b))
            break

    if heap:
        ans+=heapq.heappop(heap)

print(-ans)