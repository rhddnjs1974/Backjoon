import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
############################################

n = int(input())

arr = []
for i in range(n):
    d,w = map(int,input().split())
    heapq.heappush(arr,(-d,w))

ans = 0
heap = []

for i in range(n,0,-1):
    while(arr):
        a,b = heapq.heappop(arr)
        a = -a
        if a>=i:
            heapq.heappush(heap,(-b))
        else:
            heapq.heappush(arr,(-a,b))
            break


    if heap:
        ans+=heapq.heappop(heap)

print(-ans)