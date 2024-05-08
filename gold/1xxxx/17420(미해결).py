import heapq
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

BB = []
for i in range(n):
    BB.append((B[i],i))

BB.sort()

heap = []

for i in range(n):
    heapq.heappush(heap,(A[i],i))

now = 0
ans = 0
while(heap):
    a,b = heapq.heappop(heap)

    arr2 = [(a,b)]
    while(heap):
        x,y = heapq.heappop(heap)
        if x==a:
            arr2.append((x,y))
        else:
            heapq.heappush(heap,(x,y))
            break

    if a < BB[now][0]:
        for i,j in arr2:
            tt = BB[now][0]-a
            tt //= 30
            tt += 1
            heapq.heappush(heap,(i+tt*30,j))
            ans += tt
        continue

    flag = 0
    for i,j in arr2:
        if j == BB[now][1] or BB[now][0]==B[j]:
            flag = 1
            k = j

    if flag==0:
        for i,j in arr2:
            heapq.heappush(heap,(i+30,j))
            ans += 1
    else:
        for i,j in arr2:
            if k!=j:
                heapq.heappush(heap,(i,j))
            else:
                now+=1

print(ans)