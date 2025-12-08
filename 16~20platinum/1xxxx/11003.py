import sys
input = sys.stdin.readline
import heapq

n, l = map(int,input().split())
A = list(map(int,input().split()))
heap = []

for i in range(n):
    heapq.heappush(heap,(A[i],i))
    while(True):
        value, when = heapq.heappop(heap)
        if when>i-l:
            print(value,end=" ")
            heapq.heappush(heap,(value,when))
            break

