import sys
input = sys.stdin.readline
import heapq
n = int(input())
mih = []
mah = []
d = [0]*100001
for i in range(n):
    p,l = map(int,input().split())
    d[p] = l
    heapq.heappush(mih,(l,p))
    heapq.heappush(mah,(-l,-p))
m = int(input())
s = [0]*100001

for i in range(m):

    x, *a = input().split()
    if x=="recommend":
        if a[0]=="1":
            while(True):
                l,p = heapq.heappop(mah)
                if s[-p]==0 and d[-p]==-l:
                    print(-p)
                    heapq.heappush(mah,(l,p))
                    break
        else:
            while(True):
                l,p = heapq.heappop(mih)
                if s[p]==0 and d[p]==l:
                    print(p)
                    heapq.heappush(mih,(l,p))
                    break
    if x=="add":
        p = int(a[0])
        l = int(a[1])
        d[p] = l
        heapq.heappush(mih,(l,p))
        heapq.heappush(mah,(-l,-p))
        s[p] = 0
    if x=="solved":
        p = int(a[0])
        s[p] = 1