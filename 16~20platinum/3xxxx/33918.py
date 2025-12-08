import sys
input = sys.stdin.readline
import heapq

N,M,C,D = map(int,input().split())
B = list(map(int,input().split()))

dp = [[0]*(M+1) for i in range(N)] #dp[t][k] : t초에 온도 k로 했을때 최대값

for i in range(M+1):
    dp[0][i] = M-abs(B[0]-i)

for t in range(1,N):
    heap = []
    for k in range(D):
        heapq.heappush(heap,(-dp[t-1][k],k))
    
    for k in range(D,M+1+D):

        if k<M+1:
            heapq.heappush(heap,(-dp[t-1][k],k))
        
        temp = []
        while(True):
            value, when = heapq.heappop(heap)
            
            if when>k-D-D-1:
                if ( when-(k-D) )%C==0:
                    dp[t][k-D] = -value+M-abs(B[t]-(k-D))
                    heapq.heappush(heap,(value,when))
                    for a,b in temp:
                        heapq.heappush(heap,(a,b))
                    break
                else:
                    temp.append((value,when))

print(max(dp[-1]))