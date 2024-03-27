import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
############################################

n = int(input())
leftheap = []
rightheap = []

for i in range(n):
    a = int(input())
    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap,-a)
    else:
        heapq.heappush(rightheap,a)

    if leftheap and rightheap:
        if -leftheap[0]>rightheap[0]:
            l = heapq.heappop(leftheap)
            r = heapq.heappop(rightheap)
            heapq.heappush(leftheap,-r)
            heapq.heappush(rightheap,-l)

    print(-leftheap[0])
