import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))

    dic = {}
    for i in A:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    heap = [0,0]
    
    even = 0
    even_n = 0
    
    for i in dic:
        if dic[i]%2==0:
            even += dic[i]
            even_n += (i*dic[i])
        else:
            even += dic[i]-1
            even_n += (i*dic[i]-i)
            heapq.heappush(heap,-i)
        
    if even==0:
        print(0)
        continue
    
    a = -heapq.heappop(heap)
    flag= 0
    while(heap):
        b = a
        a = -heapq.heappop(heap)
        if b>= even_n + a:
            continue
        
        if even==2 and b+a==0:
            continue
        print(b+a+even_n)
        flag= 1
        break
    if flag==0:
        print(0)