import sys
input = sys.stdin.readline
import heapq

N,K = map(int,input().split())
A= [0]
for _ in range(N):
    A.append(int(input()))


dp = [0]
nowsum = 0
heap = []
heapq.heappush(heap,(0,0))
for i in range(1,N+1):
    nowsum += A[i]
    heapq.heappush(heap,(-dp[i-1]+nowsum,i))

    while(True):
        value, when = heapq.heappop(heap)
        if when>i-K-1:
            dp.append(nowsum-value)
            
            heapq.heappush(heap,(value,when))
            break


print(dp[-1])
