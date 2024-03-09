import sys
input = sys.stdin.readline
import heapq
########################################

N = int(input())
heap = []
for i in range(N):
    a = list(map(int,input().split()))
    for x in a:

        heapq.heappush(heap,-x)

for i in range(N-1):
    heapq.heappop(heap)

print(-heapq.heappop(heap))