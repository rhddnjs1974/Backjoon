import sys
input = sys.stdin.readline
import heapq

N,D = map(int,input().split())
A = list(map(int,input().split()))

heap = []

dp = [0]
heapq.heappush(heap,(0,-1))
for i in range(N):

    while(True):
        value, when = heapq.heappop(heap)
        
        if when>i-D-1:
            dp.append(max(A[i]-value,A[i]))
            heapq.heappush(heap,(value,when))
            break
    heapq.heappush(heap,(-dp[i+1],i))

print(max(dp[1:]))