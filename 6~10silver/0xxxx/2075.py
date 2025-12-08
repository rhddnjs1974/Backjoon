import sys
input = sys.stdin.readline
import heapq
########################################

N = int(input())
heap = []
k=0
for i in range(N):
    a = list(map(int,input().split()))
    for x in a:
        if k<N:
            heapq.heappush(heap,x)
            k+=1
        else:
            heapq.heappush(heap,x)
            heapq.heappop(heap)



print(heapq.heappop(heap))