import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    heap=[]
    n = int(input())
    for i in list(map(int,input().split())):
        heapq.heappush(heap,i)
    ans =0
    while(len(heap)>=2):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        ans+= (x+y)

        heapq.heappush(heap,x+y)
    print(ans)