import sys
import heapq
input = sys.stdin.readline

c,n = map(int,input().split())
chiken = []
for i in range(c):
    chiken.append(int(input()))
chiken.sort()

heap = []
for i in range(n):
    a,b = map(int,input().split())
    heapq.heappush(heap,(b,a))

ans=0
while(heap):
    end,start = heapq.heappop(heap)
    for i in range(c):
        if start<=chiken[i]<=end:
            chiken[i] = 0
            ans+=1
            break

print(ans)