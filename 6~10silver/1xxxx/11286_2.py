import sys
input = sys.stdin.readline
import heapq

heap =[]

n = int(input())
for i in range(n):
    x = int(input())
    if x!=0:
        heapq.heappush(heap,(abs(x),x))
    else:
        if len(heap)==0:
            print(0)
        else:
            t = heapq.heappop(heap)
            print(t[1])
        