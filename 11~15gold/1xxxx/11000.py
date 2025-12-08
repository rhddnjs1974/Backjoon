import sys
input = sys.stdin.readline
import heapq
n = int(input())
heap = []
for _ in range(n):
    a,b = map(int,input().split())
    heapq.heappush(heap,(b,a))

ans=0

while(heap):
    ans+=1
    arr=[]
    now=0
    while(heap):
        T,S = heapq.heappop(heap)
        if S>=now:
            now = T
        else:
            arr.append((T,S))

    for t,s in arr:
        heapq.heappush(heap,(t,s))
    
print(ans)