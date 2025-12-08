import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    m = int(input())
    ans = []
    
    arr = []
    for x in range((m//10)+1):
        a= list(map(int,input().split()))
        for b in a:
            arr.append(b)
    
    lheap = []
    rheap = []
    
    now = arr[0]
    ans.append(now)
    for x in range(1,m):
        num = arr[x]
        if num>now:
            heapq.heappush(lheap,num)
        else:
            heapq.heappush(rheap,-num)
        
        if x%2==0:
            if len(lheap)==len(rheap):
                ans.append(now)
            elif len(lheap)>len(rheap):
                heapq.heappush(rheap,-now)
                now = heapq.heappop(lheap)
                ans.append(now)
            else:
                heapq.heappush(lheap,now)
                now = -heapq.heappop(rheap)
                ans.append(now)
                
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i],end=" ")
        if (i+1)%10==0 and i!=len(ans)-1:
            print()
    print()