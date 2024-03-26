import sys
input = sys.stdin.readline
import heapq
########################################

N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x!=0:
        heapq.heappush(heap,(abs(x),x))
    else:
        if heap:
            result = heapq.heappop(heap)
            print(result[1])
        else:
            print(0)