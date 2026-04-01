import sys
input = sys.stdin.readline
from collections import deque
import heapq

N,M,C,D = map(int,input().split())
B = list(map(int,input().split()))

dp = [[1e9]*(M+1) for i in range(N)] #dp[t][k] : t초에 온도 k로 했을때 감점 최소값

heap = []

for i in range(1,M+1):
    dp[0][i] = abs(B[0]-i)

for i in range(1,N):
    for j in range(C): #C로 나눈 나머지가 j
        if j==0:
            j=C
        q = []
        heapq.heappush(q,(dp[i-1][j],j))

        for x in range(j+C,j+D+1,C):
            if x>M:
                continue
            heapq.heappush(q,(dp[i-1][x],x))
        

        dp[i][j] = abs(B[i]-j) + q[0][0]
        
        p = j
        for x in range(j+D+C,M+1,C):
            while(q):
                if q[0][1]<x-2*D:
                    heapq.heappop(q)
                else:
                    break
                
            heapq.heappush(q,(dp[i-1][x],x))
            
            dp[i][x-D] = abs(B[i]-(x-D)) + q[0][0]
            p = x-D
        
        for x in range(p+C,M+1,C):
            while(q):
                if q[0][1]<x-D:
                    heapq.heappop(q)
                else:
                    break
            dp[i][x] = abs(B[i]-(x)) + q[0][0]

print(-min(dp[-1])+M*N)
            