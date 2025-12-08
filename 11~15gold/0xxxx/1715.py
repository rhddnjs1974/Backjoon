import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
############################################

n = int(input())
heap = []

for i in range(n):
    a = int(input())
    heapq.heappush(heap,a)

ans = 0
while(len(heap)>1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a+b
    heapq.heappush(heap,a+b)

print(ans)
